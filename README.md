# GitHub Actions Playground: simple test around GitHub Actions and environment variables.

We specify the following environment variables in GitHub, under Settings -> Secrets and variables -> Actions:
* Under Secrets, we specify `DUMMY_SECRET` with value `my_dummy_secret` (without quotes). We can't check this value anymore in the GitHub interface, because we made a secret and it won't be shown, so it's important to remember how we entered it.
* Under Variables, we specify `DUMMY_VAR` with value `my_dummy_var` (without quotes). We can check this value anytime in the GitHub interface, because it's not a secret variable, thus it is not considered sensitive to expose its value.

We check in a python script the values as follows:
```
dummy_var = os.environ.get('DUMMY_VAR')
dummy_secret = os.environ.get('DUMMY_SECRET')
if dummy_var == "my_dummy_var":
	print("Dummy var retrieved successfully")
else:
	print("Dummy var not recognized")
if dummy_secret == "my_dummy_secret":
	print("Dummy secret retrieved successfully")
else:
	print("Dummy secret not recognized")
```

We then run the CI job in the `CI.yml` config file as follows:
```
- name: Run script
run: |
  python script.py
env:
  DUMMY_SECRET: ${{ secrets.DUMMY_SECRET }}
  DUMMY_VAR: ${{ vars.DUMMY_VAR }}
```

The output of the job is as follows:
```
Run python script.py
  python script.py
  shell: /bin/bash -e {0}
  env:
    DUMMY_SECRET: ***
    DUMMY_VAR: my_dummy_var
Dummy var retrieved successfully
Dummy secret retrieved successfully
```

Important points to keep in mind:
* no need for special handling of quotes
* no need for bridging the environment variables from the yml file into the shell, such as with `export` commands or similar

