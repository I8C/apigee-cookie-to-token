var now = new Date();

var expires_in = context.getVariable("resp.expires_in");

var expireEpoch = now.setSeconds(now.getSeconds() + expires_in);

context.setVariable("resp.expires_at", expireEpoch);