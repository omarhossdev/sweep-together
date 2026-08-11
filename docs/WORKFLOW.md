# 🔄 Workflow

## User Auth

### New User Registration

1. User submits email/password OR sign in with *Google or Facebook*
2. Backend validates input 
3. Hash password -> store in DB
4. Send verification email
5. Return JWT token

### Password Reset

1. User enters his email and requests reset
2. Generate reset token
3. Email reset link
4. User click -> verify token
5. Update password -> invalidate old tokens

### Login

1. User enters his email/password OR login with *Google or Facebook*
2. Backend validates input
3. Compare the password with hashed one from DB
4. Login the user and save his token