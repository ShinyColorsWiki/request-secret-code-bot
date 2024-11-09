# request-secret-code-bot

Discord bot for QuestyCaptcha Secret-resolve things


## Installation
### Mediawiki
```php
# QuestyCaptcha things
wfLoadExtension('ConfirmEdit');
wfLoadExtension('ConfirmEdit/QuestyCaptcha');

# Settings
$keyLength = 16;
$answerLength = 16;
$secretSeed = 'this-is-super-secret-things-of-the-world';

# Initialize $wgCaptchaQuestions as an empty array
$wgCaptchaQuestions = array();

# Generate a random 16-character hexadecimal Key
$keyBytes = random_bytes($keyLength / 2); // Each byte is two hex characters
$key = bin2hex($keyBytes);

# Compute the Answer using HMAC-SHA256
$hash = hash_hmac('sha256', $key, $secretSeed);

# Take a substring of the hash as the Answer (e.g., first 16 characters)
$answer = substr($hash, 0, $answerLength);

# Now add the dynamic question and answer to $wgCaptchaQuestions[]
$wgCaptchaQuestions[] = array(
    'question' => "<code>/request_secret key:$key</code>",
    'answer' => $answer,
);

$wgCaptchaTriggers['edit']          = false;
$wgCaptchaTriggers['create']        = false;
$wgCaptchaTriggers['createtalk']    = false;
$wgCaptchaTriggers['addurl']        = false;
$wgCaptchaTriggers['createaccount'] = true;
$wgCaptchaTriggers['badlogin']      = false;
$wgGroupPermissions['user']['skipcaptcha'] = true;
```

### Bot Environment
```env
DISCORD_BOT_TOKEN=[see_documentation]
SECRET_SEED=this-is-super-secret-things-of-the-world
KEY_LENGTH=16 # same as above
ANSWER_LENGTH=16 # same as above
LOG_LEVEL=INFO
GUILD_IDS=[...]
```

### Run it
```bash
$ python run.py
```