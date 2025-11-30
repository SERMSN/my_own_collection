#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This module creates a text file with specified content

version_added: "1.0.0"

description: This module creates a text file on the remote host at the specified path with the given content.

options:
    path:
        description: The path where the file should be created.
        required: true
        type: str
    content:
        description: The content to write to the file.
        required: true
        type: str

author:
    - Student (@student)
'''

EXAMPLES = r'''
# Create a file with content
- name: Create a test file
  my_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "Hello World!"
'''

RETURN = r'''
path:
    description: The path where the file was created.
    type: str
    returned: always
content:
    description: The content that was written to the file.
    type: str
    returned: always
changed:
    description: Whether the file was created or modified.
    type: bool
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    # ОБРАТИТЕ ВНИМАНИЕ: используем только path и content, убрали name и new
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    try:
        # Check if file exists and content is the same
        file_exists = os.path.exists(path)
        if file_exists:
            with open(path, 'r') as f:
                existing_content = f.read()
            if existing_content == content:
                result['changed'] = False
            else:
                with open(path, 'w') as f:
                    f.write(content)
                result['changed'] = True
        else:
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=f"Failed to create file: {str(e)}", **result)

def main():
    run_module()

if __name__ == '__main__':
    main()
