# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def has_permission(page):
    def permission(username):
        if username.lower() == "admin":
            return f"'{username}' has access to {page}."
        else:
            return f"'{username}' doesn`t have access to {page}."
    return permission
check_admin_page_permission = has_permission("Admin Page")
print(check_admin_page_permission('admin'))
print(check_admin_page_permission('StaniSlavuS'))