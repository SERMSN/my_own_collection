# My Own Namespace - Yandex Cloud ELK Collection

This collection contains a custom module for creating files with specified content.

## Modules

### my_own_module

Creates a text file on the remote host with specified content.

#### Parameters
- `path` (required): Path where to create the file
- `content` (required): Content to write to the file

#### Examples
```yaml
- name: Create test file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "Hello World"
