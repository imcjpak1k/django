
> python -m venv venv

> pip install django
Collecting django
  Downloading https://files.pythonhosted.org/packages/2b/5a/4bd5624546912082a1bd2709d0edc0685f5c7827a278d806a20cf6adea28/Django-3.1-py3-none-any.whl (7.8MB)
    100% |████████████████████████████████| 7.8MB 2.7MB/s
Collecting sqlparse>=0.2.2 (from django)
  Downloading https://files.pythonhosted.org/packages/85/ee/6e821932f413a5c4b76be9c5936e313e4fc626b33f16e027866e1d60f588/sqlparse-0.3.1-py2.py3-none-any.whl (40kB)
    100% |████████████████████████████████| 40kB 482kB/s
Collecting pytz (from django)
  Downloading https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl (510kB)
    100% |████████████████████████████████| 512kB 3.7MB/s
Collecting asgiref~=3.2.10 (from django)
  Downloading https://files.pythonhosted.org/packages/d5/eb/64725b25f991010307fd18a9e0c1f0e6dff2f03622fc4bcbcdb2244f60d6/asgiref-3.2.10-py3-none-any.whl
Installing collected packages: sqlparse, pytz, asgiref, django
Successfully installed asgiref-3.2.10 django-3.1 pytz-2020.1 sqlparse-0.3.1
You are using pip version 19.0.3, however version 20.2.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.


> pip install caldav
Collecting caldav
  Downloading https://files.pythonhosted.org/packages/be/fd/cdc3a42712cdef6ba8ee5ae547c61bce15d3230459a339ced24431d4aab2/caldav-0.7.1-py3-none-any.whl (41kB)
    100% |████████████████████████████████| 51kB 186kB/s
Collecting requests (from caldav)
  Using cached https://files.pythonhosted.org/packages/45/1e/0c169c6a5381e241ba7404532c16a21d86ab872c9bed8bdcd4c423954103/requests-2.24.0-py2.py3-none-any.whl
Collecting lxml (from caldav)
  Downloading https://files.pythonhosted.org/packages/bd/a3/4b377aaf02ea39585b81ad9f630226e296d983e9a94d7b78a4bc5e27226d/lxml-4.5.2-cp37-cp37m-win_amd64.whl (3.5MB)
    100% |████████████████████████████████| 3.5MB 2.5MB/s
Collecting six (from caldav)
  Downloading https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
Collecting vobject (from caldav)
  Downloading https://files.pythonhosted.org/packages/da/ce/27c48c0e39cc69ffe7f6e3751734f6073539bf18a0cfe564e973a3709a52/vobject-0.9.6.1.tar.gz (58kB)
    100% |████████████████████████████████| 61kB 991kB/s
Collecting chardet<4,>=3.0.2 (from requests->caldav)
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting idna<3,>=2.5 (from requests->caldav)
  Using cached https://files.pythonhosted.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests->caldav)
  Using cached https://files.pythonhosted.org/packages/5e/c4/6c4fe722df5343c33226f0b4e0bb042e4dc13483228b4718baf286f86d87/certifi-2020.6.20-py2.py3-none-any.whl
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests->caldav)
  Downloading https://files.pythonhosted.org/packages/9f/f0/a391d1463ebb1b233795cabfc0ef38d3db4442339de68f847026199e69d7/urllib3-1.25.10-py2.py3-none-any.whl (127kB)
    100% |████████████████████████████████| 133kB 2.8MB/s
Collecting python-dateutil>=2.4.0 (from vobject->caldav)
  Downloading https://files.pythonhosted.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl (227kB)
    100% |████████████████████████████████| 235kB 2.4MB/s
Installing collected packages: chardet, idna, certifi, urllib3, requests, lxml, six, python-dateutil, vobject, caldav
  Running setup.py install for vobject ... done
Successfully installed caldav-0.7.1 certifi-2020.6.20 chardet-3.0.4 idna-2.10 lxml-4.5.2 python-dateutil-2.8.1 requests-2.24.0 six-1.15.0 urllib3-1.25.10 vobject-0.9.6.1
You are using pip version 19.0.3, however version 20.2.1 is available.



>pip install icalendar
Collecting icalendar
  Downloading https://files.pythonhosted.org/packages/20/f2/f600e9aa510ab6e052b0344d7f3a4d6124229c74a922d8dea9b15e1aaf2b/icalendar-4.0.6-py2.py3-none-any.whl (74kB)
    100% |████████████████████████████████| 81kB 230kB/s
Requirement already satisfied: pytz in c:\users\imcjp\workspace\vscode\django\openapi\venv\lib\site-packages (from icalendar) (2020.1)
Requirement already satisfied: python-dateutil in c:\users\imcjp\workspace\vscode\django\openapi\venv\lib\site-packages (from icalendar) (2.8.1)
Requirement already satisfied: six>=1.5 in c:\users\imcjp\workspace\vscode\django\openapi\venv\lib\site-packages (from python-dateutil->icalendar) (1.15.0)
Installing collected packages: icalendar
Successfully installed icalendar-4.0.6
You are using pip version 19.0.3, however version 20.2.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.