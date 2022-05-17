var n = new Date();
n = n.setSeconds(n.getSeconds());
var expires = context.getVaribale("resp.expires_in");


if(n <= expires)
{
    //context.setVariable("URL")    
}

