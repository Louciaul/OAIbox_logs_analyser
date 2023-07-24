# How to get and transform the OAIBox logs in a beautiful useful csv for analysing data (V 1.0)

## Summary

1) Purpose of this script

2) What does the code do

3) How to use it

4) How to get the logs from your OAIBox

5) Contact in case somethings is wrong

6) License

### 1) Purpose of this script

To anyone who wants to use the OAIbox, you can in fact create your own script to parse the json file but here is one in case you want to use a CSV for analysing your data

you can see an exemple of result in [result_test.csv](csv/result_test.csv) from [30mins.json](json/30mins.json)

Be aware that if the format of OAIbox logs change, this script will then be depreciated

This code allows you to also recreate diverse graphs from the data
you can find them in [graph](graph) folder


### 2) What does the code do

You will there find 2 scripts:

- first one convert a json into a csv:

    It takes a .json oaibox log file and return a .csv file.

    You can find an example result in the folder (test.csv)

    For each line (packet) you'll find values for a specified Rnti:

    - Id
    - Frame
    - Slot
    - Pci
    - Timestamp
    - Dl Bytes
    - Dl Mcs
    - Dl Bler
    - Ul Bytes
    - Ul Mcs
    - Ri
    - Pmi
    - Phr
    - Pcmax
    - Rsrp
    - Rsrq
    - Sinr
    - Rssi
    - Cqi
    - Pucch Snr
    - Pusch Snr

    The script also delete line of logs with no Rnti (ue) inside.

- Second most of the graphs with the csv file. You can then use filter to get more precise result

### 3) How to use it

in the OAIBOX_LOGS_ANALYZER FOLDER:

To get your csv file from the json logs:

```bash
python src/json_to_csv.py your-logs.json name-of-your-result-file.csv
```

NB: your json need to be in the json folder to succesfully work. your csv file will be in the csv folder also.

---
To get your graph:

NB: your csv file need to be in the "csv" folder to the code to work


```bash
python src/main.py file.csv [-s (int)] [-e (int)] [-r1 (string)] [-r2 (string)] 
```


Avaible options:

-s option: to change the starting timer of the data (for example if you don't want the 5 first minutes on your graph just use "-s 300" (time is in second))

-e option: to change the ending timer of the data (for example if you don't want the 5 last minutes on your graph just use "-e 300" (time is in second))

-r1 option: if you want to select only one rnti specifically (for example if you want to see only rnti "4ac8" use "r1 4ac8)

-r2 option: (only if r1 used) if you want to select a second rnti


### 4) How to get the logs of your OAIbox

- Go on the OAIbox dashboard

- Choose the Box that you want to collect the data

- Click on the NG-RAN icon (only if started)

- Then on the left of the dashboard click on the button to download the logs



### 5) Version

~~V 0.1 - 06/07/2023~~

V 1.0 - 24/07/2023:

added:

- Graphs and options

### 6) License

This project is under the GNU GENERAL PUBLIC LICENSE-3.0 new or revised license. Please read the [LICENSE](LICENSE) file.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

