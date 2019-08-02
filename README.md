# tap-copper

Author: Jacob Werderits (jacob@fishtownanalytics.com)

This is a [Singer](http://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

It:
- Generates a catalog of available data in Copper
- Extracts the following resources:
  - [Accounts](https://developer.copper.com/?version=latest#0add3728-327d-4b16-82a8-40b54d176fa9)
  - [Users](https://developer.copper.com/?version=latest#0add3728-327d-4b16-82a8-40b54d176fa9)
  - [Leads](https://developer.copper.com/?version=latest#fa0e5345-3ec3-41ae-acf1-700c8fb27a3a)
  - [People](https://developer.copper.com/?version=latest#4db472db-00a1-45ab-9185-c4660916aac0)
  - [Companies](https://developer.copper.com/?version=latest#84b5bc50-275d-4a69-a004-6e3f3f077583)
  - [Opportunities](https://developer.copper.com/?version=latest#1cd9465f-bd88-4a2c-91fc-ad2d41ecc540)
  - [Activities](https://developer.copper.com/?version=latest#2c9a03e2-bb9f-431b-8d22-3ff741d8dee3)
  - [Projects](https://developer.copper.com/?version=latest#ef473fd5-7e1c-4ca7-9bc6-12c9e025afd2)
  - [Tasks](https://developer.copper.com/?version=latest#0a0059cd-6aa6-4937-a5ec-47c23319271e)

### Quick Start

1. Install

```bash
git clone git@github.com:fishtown-analytics/tap-copper.git
cd tap-copper
pip install -e .
```

2. Get an API key

Create a Copper [Authentication Token](https://developer.copper.com/?version=latest#authentication). Tokens are tied to a user's email (the user's permissions determine the data avaialable). After receiving an API token keep it somewhere safe, as you'll need it to authenticate requests. See "Create the config file" below for more information on using this API Token,

3. Create the config file.

There is a template you can use at `config.json.example`, just copy it to `config.json` in the repo root and insert your token and email

4. Run the application to generate a catalog.

```bash
tap-copper -c config.json --discover > catalog.json
```

5. Select the tables you'd like to replicate

Step 4 generates a a file called `catalog.json` that specifies all the available endpoints and fields. You'll need to open the file and select the ones you'd like to replicate. See the [Singer guide on Catalog Format](https://github.com/singer-io/getting-started/blob/c3de2a10e10164689ddd6f24fee7289184682c1f/BEST_PRACTICES.md#catalog-format) for more information on how tables are selected.

6. Run it!

```bash
tap-copper -c config.json --catalog catalog.json
```

Copyright &copy; 2019 Fishtown Analytics
