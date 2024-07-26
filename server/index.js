const express =  require("express");
const cors = require("cors");

const app = express();

app.use(express.json());
app.use(cors({origin:true}));

app.post("/authenticate", async(req,res) =>{
    const {username} = req.body;
    return res.json({username:username, secret: "sha256..."});

});

app.listen(process.env.PORT || 3001, () => console.log("app is available on local host port http://localhost:3001"))