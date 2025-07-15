

\# 📌 MyRateb Sanctions Screening System



A Python-based automated compliance workflow built with \*\*Zoho Catalyst\*\*, designed to:

\- Cross-check new employee records against the \*\*UN Sanctions List\*\*

\- Notify compliance officers via \*\*email\*\* when a match is found

\- Automatically \*\*update account status\*\* in Zoho CRM from \_Open\_ to \_Blocked\_



---



\## 🚀 Features



✅ Fetches employee data from Zoho CRM  

✅ Parses and compares names against a provided UN XML alias list  

✅ Sends notification emails upon match detection  

✅ Blocks associated account by updating a custom CRM field (`Account\_Status`)  

✅ Built using \*\*Zoho Catalyst\*\*, Python 3.9, and RESTful APIs



---



\## 🏗️ Tech Stack



\- \*\*Zoho Catalyst Functions\*\* (Python runtime)

\- \*\*Zoho CRM API\*\* (Accounts module)

\- \*\*Zoho Mail API\*\*

\- \*\*UN Sanctions List XML\*\*

\- \*\*Python\*\*: `requests`, `json`, `zcatalyst\_sdk`



---



\## 📁 Project Structure



```

├── functions/

│   ├── employee\_workflow/

│   │   └── main.py              # Core logic: fetch, compare, notify

│   ├── fetch\_employee/

│   │   └── main.py              # Fetches latest CRM employee

│   ├── xml\_parser/

│   │   └── main.py              # Parses the UN XML list

│   ├── update\_account\_status/

│   │   └── main.py              # Updates CRM field if matched

├── lib/

├── .env                         # 🔒 Contains API tokens \& secrets

├── .gitignore

├── README.md

```



---



\## 🔒 Environment Variables



You must provide a `.env` file at the root of your project with the following:



```env

ZOHO\_CLIENT\_ID=xxxxxxxx

ZOHO\_CLIENT\_SECRET=xxxxxxxx

ZOHO\_REFRESH\_TOKEN=xxxxxxxx

ZOHO\_ACCESS\_TOKEN=xxxxxxxx

ZOHO\_MAIL\_ACCOUNT\_ID=xxxxxxxx

```



> ✅ A `.env.example` is included for reference.



---



\## ⚙️ How It Works



1\. \*\*New employee entry is created\*\* in Zoho CRM.

2\. `employee\_workflow` function:

&nbsp;  - Fetches the latest employee using `fetch\_employee`

&nbsp;  - Extracts and parses aliases from the UN XML list using `xml\_parser`

&nbsp;  - Checks for a match (case-insensitive)

3\. If a \*\*match is found\*\*:

&nbsp;  - Sends a \*\*warning email\*\* to the compliance team

&nbsp;  - Calls `update\_account\_status` with the record ID

&nbsp;  - Updates the `Account\_Status` field from `"Open"` to `"Blocked"`



---



\## 📧 Email Sample



Subject: `Match Found in Sanctions List`



```

A blacklisted user has registered on My Rateb with the following details:



Civil ID - 285052101234

Name - Abdul Latif Mansoor

DOB - 1985-05-21

Mobile number - 50012345



The account is now blocked to be reviewed by compliance.

```



---



\## ✅ Sample Match Flow



```bash

> POST /server/employee\_workflow/

→ \[✓] Matched alias found: "Abdul Latif Mansoor"

→ \[✓] Email sent to compliance

→ \[✓] Account\_Status updated to "Blocked"

```



---



\## 📦 Deployment



1\. Install the Catalyst CLI:

&nbsp;  ```bash

&nbsp;  npm install -g zcatalyst-cli

&nbsp;  ```



2\. Login to Zoho and initialize:

&nbsp;  ```bash

&nbsp;  catalyst init

&nbsp;  catalyst deploy

&nbsp;  ```



3\. Monitor logs:

&nbsp;  ```bash

&nbsp;  catalyst functions:serve

&nbsp;  ```



---


---



\## 🛡️ License



This project is for educational and professional portfolio use. Not affiliated with Zoho Corporation.



\# 📌 MyRateb Sanctions Screening System



A Python-based automated compliance workflow built with \*\*Zoho Catalyst\*\*, designed to:

\- Cross-check new employee records against the \*\*UN Sanctions List\*\*

\- Notify compliance officers via \*\*email\*\* when a match is found

\- Automatically \*\*update account status\*\* in Zoho CRM from \_Open\_ to \_Blocked\_



---



\## 🚀 Features



✅ Fetches employee data from Zoho CRM  

✅ Parses and compares names against a provided UN XML alias list  

✅ Sends notification emails upon match detection  

✅ Blocks associated account by updating a custom CRM field (`Account\_Status`)  

✅ Built using \*\*Zoho Catalyst\*\*, Python 3.9, and RESTful APIs



---



\## 🏗️ Tech Stack



\- \*\*Zoho Catalyst Functions\*\* (Python runtime)

\- \*\*Zoho CRM API\*\* (Accounts module)

\- \*\*Zoho Mail API\*\*

\- \*\*UN Sanctions List XML\*\*

\- \*\*Python\*\*: `requests`, `json`, `zcatalyst\_sdk`



---



\## 📁 Project Structure



```

├── functions/

│   ├── employee\_workflow/

│   │   └── main.py              # Core logic: fetch, compare, notify

│   ├── fetch\_employee/

│   │   └── main.py              # Fetches latest CRM employee

│   ├── xml\_parser/

│   │   └── main.py              # Parses the UN XML list

│   ├── update\_account\_status/

│   │   └── main.py              # Updates CRM field if matched

├── lib/

├── .env                         # 🔒 Contains API tokens \& secrets

├── .gitignore

├── README.md

```



---



\## 🔒 Environment Variables



You must provide a `.env` file at the root of your project with the following:



```env

ZOHO\_CLIENT\_ID=xxxxxxxx

ZOHO\_CLIENT\_SECRET=xxxxxxxx

ZOHO\_REFRESH\_TOKEN=xxxxxxxx

ZOHO\_ACCESS\_TOKEN=xxxxxxxx

ZOHO\_MAIL\_ACCOUNT\_ID=xxxxxxxx

```



> ✅ A `.env.example` is included for reference.



---



\## ⚙️ How It Works



1\. \*\*New employee entry is created\*\* in Zoho CRM.

2\. `employee\_workflow` function:

&nbsp;  - Fetches the latest employee using `fetch\_employee`

&nbsp;  - Extracts and parses aliases from the UN XML list using `xml\_parser`

&nbsp;  - Checks for a match (case-insensitive)

3\. If a \*\*match is found\*\*:

&nbsp;  - Sends a \*\*warning email\*\* to the compliance team

&nbsp;  - Calls `update\_account\_status` with the record ID

&nbsp;  - Updates the `Account\_Status` field from `"Open"` to `"Blocked"`



---



\## 📧 Email Sample



Subject: `Match Found in Sanctions List`



```

A blacklisted user has registered on My Rateb with the following details:



Civil ID - 285052101234

Name - Abdul Latif Mansoor

DOB - 1985-05-21

Mobile number - 50012345



The account is now blocked to be reviewed by compliance.

```



---



\## ✅ Sample Match Flow



```bash

> POST /server/employee\_workflow/

→ \[✓] Matched alias found: "Abdul Latif Mansoor"

→ \[✓] Email sent to compliance

→ \[✓] Account\_Status updated to "Blocked"

```



---



\## 📦 Deployment



1\. Install the Catalyst CLI:

&nbsp;  ```bash

&nbsp;  npm install -g zcatalyst-cli

&nbsp;  ```



2\. Login to Zoho and initialize:

&nbsp;  ```bash

&nbsp;  catalyst init

&nbsp;  catalyst deploy

&nbsp;  ```



3\. Monitor logs:

&nbsp;  ```bash

&nbsp;  catalyst functions:serve

&nbsp;  ```

