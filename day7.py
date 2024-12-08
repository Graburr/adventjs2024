# 5 stars
def fix_packages(packages):
    while '(' in packages:
        start = packages.rfind('(')
        end = packages.find(')', start)
        
        inner = packages[start+1:end][::-1]
        packages = packages[:start] + inner + packages[end+1:]
    
    return packages