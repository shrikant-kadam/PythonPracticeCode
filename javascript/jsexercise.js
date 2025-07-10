//initialize variables
FirstName = prompt("Enter your First Name : ")
LastName = prompt("Enter your Last Name : ")
Age = prompt("Enter your Age : ")
Height = prompt("Enter your Height : ")
City = prompt("Enter your City : ")
alert("Thank you for information...!")

//check all conditions
NameCond = null
AgeCond = null
HeightCond = null
CityCond = null

//Logic
if (FirstName[0] === LastName[0]){
NameCond = true
} else{
NameCond = false
}

if (Age > 18){
AgeCond = true
} else{
AgeCond = false
}

if (Height > 170){
HeightCond = true
} else{
HeightCond = false
}

if (City[City.length-1] === "e"){
CityCond = true
} else{
CityCond = false
}

//all conditions checked
if(NameCond && AgeCond && HeightCond && CityCond){
console.log("All information is correct..!")
}else{
console.log("Wrong Information...")
}
