# Tests Generator
This python modules allow automatic generation of unit test code for <b>Django</b> python framework.
In order to autogenerate the code you need to add a <b>test_urls.json</b> into the app folder you want the code to be
autogenerated.

The file should follow this pattern:
```
{
    "urls": [
        {
            "name": "name_of_the_test",
            "url": "url in which generate the test"
        },
        ...
    ]
}
```
