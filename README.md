# Linux Package Print Diff

Leverage this [repo](https://github.com/etho201/vagrant-boxes/tree/main/uln-search) first to obtain a list of ULN packages.

1. Strip version numbers from needed packages:

    ```bash
    python3 scrub.py -2 -i work_dir/packages.required
    ```
    > scrub.py `-2` filters out the version number after the package name
    >
    > Example: `cups-2.3.3op2-11.fc34.x86_64` becomes `cups`

2. Filter out only the package names from uln_packages:

    ```bash
    python3 scrub.py -1 -i work_dir/uln-packages.txt
    ```

    > scrub.py `-1` filters out everthing after the first period of a package name
    >
    > Example: `cups.x86_64` becomes `cups`

3. List any packages that are missing from the ULN repository:

    ```bash
    python3 compare.py -a work_dir/scrubbed-packages.required -b work_dir/scrubbed-uln-packages.txt
    ```

    > This will create a new file called: `missing-scrubbed-packages.required` with the results.