def change(org: str):
    if '\\' in org:
        dirs = org.split('\\');
        new_dir = '';
        first_loop = True;
        for dir in dirs:
            if first_loop: 
                first_loop = False;
                new_dir += dir;
                continue;
            new_dir += '/';
            new_dir += dir;
    elif '/' in org:
        dirs = org.split('/');
        new_dir = '';
        first_loop = True;
        for dir in dirs:
            if first_loop: 
                first_loop = False;
                new_dir += dir;
                continue;
            new_dir += '\\';
            new_dir += dir;
    else:
        return org;
    
    return new_dir;
