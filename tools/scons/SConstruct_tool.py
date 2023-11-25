def ADir(path):
    return Dir(os.path.join(env['component_dir'], path))
def AFile(file):
    return File(os.path.join(env['component_dir'], file))

def AGlob(path):
    return Glob(os.path.join(env['component_dir'], path))

def append_srcs_dir(*directories):
    source_files = []
    import os
    supported_extensions = ['.c', '.cpp', '.S']

    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                _, file_extension = os.path.splitext(file)
                if file_extension in supported_extensions:
                    source_files.append(os.path.join(root, file))

    return source_files

def register_component(SRCS=[], INCLUDE=[], PRIVATE_INCLUDE=[], REQUIREMENTS=[], STATIC_LIB=[], DYNAMIC_LIB=[], DEFINITIONS=[], DEFINITIONS_PRIVATE=[], LDFLAGS=[], LINK_SEARCH_PATH=[], project='static', target='main'):
    component_info = {'SRCS': SRCS,
                      'INCLUDE': INCLUDE,
                      'PRIVATE_INCLUDE': PRIVATE_INCLUDE,
                      'REQUIREMENTS': REQUIREMENTS,
                      'STATIC_LIB': STATIC_LIB,
                      'DYNAMIC_LIB': DYNAMIC_LIB,
                      'DEFINITIONS': DEFINITIONS,
                      'DEFINITIONS_PRIVATE': DEFINITIONS_PRIVATE,
                      'LDFLAGS': LDFLAGS,
                      'LINK_SEARCH_PATH': LINK_SEARCH_PATH,
                      'target': target,
                      'project': project
                      }
    env['COMPONENTS'].append(component_info)