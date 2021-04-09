# FLAME GPU Website

This repository contains the source for the FLAME GPU website, built with [Jekyll](https://jekyllrb.com/), and using the [Minimal Mistakes theme](https://github.com/mmistakes/minimal-mistakes).

The website is hosted on GitHub Pages and can be found at [https://flamegpu.github.io](https://flamegpu.github.io).

## Development

### Install Dependencies

1. Install Ruby
    * On Windows, this installer can be used [https://rubyinstaller.org/](https://rubyinstaller.org/)
    * On Linux, follow the instructions according to your distribution e.g. for Debian/Ubuntu:
        ```sh
        sudo apt install ruby-full
        ```
2. Install `bundler` (via a terminal):
   ```sh
   gem install bundler jekyll
   ```
3. Install other dependencies:
    ```sh
    cd path/to/clone/of/this/repo
    bundle config set path vendor/bundle
    bundle install
    ```

**Note:** if you get an error related to the `public_suffix` package, try installing and updating bundler before rebuilding the site:

```sh
gem install public_suffix --version 3.0.3
bundler update
```

### Updating Dependencies

Ensure ruby packages are up to date, to avoid differences between local and GitHub/GitHub Actions builds:

```sh
bundle update --all
```

### Serving a Local Copy of the Website

To build and serve a local copy of the website, run

```sh
bundle exec jekyll serve
```

The website can then be found at `http://127.0.0.1:4000`

Note that if you are running Ruby 2.7 then you [will see lots of deprecation warnings until Jekyll 4.1 is released](https://github.com/jekyll/jekyll/pull/7948#issuecomment-584132037).

### Building HTML files

```sh
bundle exec jekyll build
```

Generated HTML files can be found in `_site`.

## Publications and Citations

The website uses a data file to dynamically display details of FLAME GPU publications and citations respectively. To populate these data files there is a provided python script (`citations.py`) which uses the [scholarly](https://pypi.org/project/scholarly/) Pythoin package to scrape the details from the web. To run this script use the instructions below. 

*Note: The script is not run as part of the site build as it will likely fail due to aggressive bot detection*

### Install dependencies

You can either install the scholarly Python package or do this via an environment manager such as conda. E.g.

```sh
conda create --name scholarly --file requirements.txt
```

Then active your conda environment

```sh
activate scholarly
```

## Configuring the FLAME GPU papers

The title of each FLAME GPU publication is hard coded in the `citations.py` file within the `flame_pubs` array. Each of these paper titles will have the full publication details retrieved form the web which will be stored in json format within `data\publications.yml`.

The 'data\citations.yml' file will be populated by retrieving papers which site any of the FLAME GPU publications (e.g. papers in `flame_pubs`). The citations are then ordered by number of citations as a rough metric of the significance of the paper (more citations is better).

## Running the citations script

In order to run the citations scrip (from the activated conda environment) run the following;

```sh
python citations.py
```

**Important**: The scholarly library uses web scraping and google scholar is very aggressive towards bots. It is highly likely that when you script runs you will get a pop-up browser window to complete a captcha to proceed. Using the scraping code may lead to IP blocking so do so at your own risk (or via a proxy/VPN).
