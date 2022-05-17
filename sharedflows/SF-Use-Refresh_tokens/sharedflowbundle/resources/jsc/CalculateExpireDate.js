var now = new Date();

var expires_in = context.getVariable("SF-Use-Refresh_tokens.expires_in");

var expireEpoch = now.setSeconds(now.getSeconds() + expires_in);

context.setVariable("out.SF-Use-Refresh_tokens.expires_at", expireEpoch);