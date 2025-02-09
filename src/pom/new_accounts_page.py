from playwright.sync_api import Page
import time

class NewAccountPage:
    def __init__(self, page: Page):
        self.page = page

    def create_savings_account(self):
        self.page.locator('//*[@id="leftPanel"]/ul/li[1]/a').click()
        time.sleep(3)
        self.page.get_by_role("combobox").first.select_option("1")
        self.page.locator('//*[@id="openAccountForm"]/form/div/input').click()
        self.page.wait_for_selector('//*[@id="leftPanel"]/ul/li[2]/a', timeout=5000)
        self.page.locator('//*[@id="leftPanel"]/ul/li[2]/a').click()
        self.page.wait_for_selector("a[href^='activity.htm']", timeout=5000)
        links = self.page.locator("a").all()
        activity_links = [
            link.get_attribute("href") for link in links if link.get_attribute("href") and link.get_attribute("href").startswith("activity.htm")
        ]
        if not activity_links:
            raise ValueError("No account activity links found! Account might not have been created.")
        last_link = activity_links[-1]
        last_id = last_link.split("id=")[-1]
        print("Here is the account ID:", last_id)
        return last_id  


    def calculations(self):
        self.page.wait_for_selector('//*[@id="accountTable"]/tbody/tr', timeout=5000)
        rows = self.page.locator('//*[@id="accountTable"]/tbody/tr')
        all_td_values = []
        for row in rows.all():
            td_values = row.locator("td").all()
            td_texts = [td.inner_text() for td in td_values]
            all_td_values.append(td_texts)
        if not all_td_values:
            print("No account data found!")
            return []
        account_ids = [item[0] for item in all_td_values if item and item[0].isdigit()]
        middle_values = [item[1] for item in all_td_values if len(item) > 1 and item[1] not in ['Total', '\xa0']]
        numeric_values = [float(value.replace('$', '').replace(',', '')) for value in middle_values[:-1]] if len(middle_values) > 1 else []

        print("Account IDs:", account_ids)
        print("The Amount Of Balance Available In Each Account:", numeric_values)

        if len(all_td_values) > 1 and len(all_td_values[-1]) > 1:
            expected_total = float(all_td_values[-1][1].replace('$', '').replace(',', ''))
            calculated_total = sum(numeric_values)
            assert calculated_total == expected_total, "Balance mismatch!"
        return account_ids

    def transfer_funds(self, account_ids):
        print(f"Checking available accounts: {len(account_ids)}")
        if len(account_ids) < 2: 
            print("Not enough accounts for transfer. Creating another account...")
            self.create_savings_account()  
            time.sleep(5)  
            account_ids = self.calculations()
            if len(account_ids) < 2:
                print("Account creation failed or did not reflect in UI. Transfer aborted.")
                return
        if len(account_ids) < 2:
            print("⚠️ Only one account available. Cannot perform transfer.")
            return
        from_account = account_ids[0]
        print("From Account:"account_ids[0])
        to_account = account_ids[1]
        print("Destination Account",account_ids[1])
        print(f"✅ Transferring $1000 from {from_account} to {to_account}...")
        self.page.locator('//*[@id="leftPanel"]/ul/li[3]/a').click()
        self.page.locator('//*[@id="amount"]').fill("1000")
        self.page.locator('//*[@id="fromAccountId"]').select_option(from_account)
        self.page.locator('//*[@id="toAccountId"]').select_option(to_account)
        self.page.locator('//*[@id="transferForm"]/div[2]/input').click()
        print("✅ Transfer successful!")


    def pay_bill(self, account_ids):
        if not account_ids:
            print("No accounts available for bill payment.")
            return

        from_account = account_ids[0]  
        self.page.locator('//*[@id="leftPanel"]/ul/li[4]/a').click()
        print(f"Paying $500 from Account {from_account} to Electricity Company...")
        self.page.locator('//*[@id="billpayForm"]/form/table/tbody/tr[1]/td[2]/input').fill("Electricity Company")
        self.page.locator('//*[@id="billpayForm"]/form/table/tbody/tr[2]/td[2]/input').fill("123 Main St")
        self.page.locator('//*[@id="billpayForm"]/form/table/tbody/tr[3]/td[2]/input').fill("New York")
        self.page.locator('//*[@id="billpayForm"]/form/table/tbody/tr[4]/td[2]/input').fill("NY")
        self.page.locator('//*[@id="billpayForm"]/form/table/tbody/tr[5]/td[2]/input').fill("10001")
        try:
            # self.page.wait_for_selector("//label[contains(text(),'Phone')]/following-sibling::input", timeout=10000)
            # self.page.locator("//label[contains(text(),'Phone')]/following-sibling::input").fill("1234567890")
            self.page.keyboard.press("Tab")  # Adjust as needed
            # Type the phone number
            self.page.keyboard.type("1234567890")
        except Exception as e:
            print(f"❌ Error: Unable to locate the Phone field - {e}")
            self.page.screenshot(path="phone_field_error.png")  # Take a screenshot for debugging
            return
        self.page.keyboard.press("Tab")  # Adjust as needed
        time.sleep(3)
        self.page.keyboard.type(from_account)
        time.sleep(3)
        self.page.keyboard.press("Tab")  # Adjust as needed
        time.sleep(3)
        self.page.keyboard.type(from_account)
        time.sleep(3)
        self.page.keyboard.press("Tab")  # Adjust as needed
        time.sleep(3)
        self.page.keyboard.type("500")
        time.sleep(3)
        self.page.locator('//*[@id="billpayForm"]/form/table/tbody/tr[14]/td[2]/input').click()
        time.sleep(10)
        assert self.page.title()
