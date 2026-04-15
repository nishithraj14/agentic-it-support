# Password Reset Policy

## Issue
User forgot password

## Steps
1. Verify identity via MFA or employee ID
2. Trigger password reset link
3. Force password change on next login

## Edge Cases
- Account locked → unlock first
- Multiple failed attempts → temporary block

## Escalation
- If identity cannot be verified
