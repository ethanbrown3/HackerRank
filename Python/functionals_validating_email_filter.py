# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
import re

def fun(email):
    # return True if email is a valid email, else return False
    pattern = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+?\.[a-zA-Z]{2,3}$')
    out = pattern.match(email)
    return out

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    _emails = []
    for _ in range(n):
        _emails.append(raw_input())

    filtered_emails = filter_mail(_emails)
    filtered_emails.sort()
    print filtered_emails
