# How to get and transform the OAIBox logs in a beautiful useful csv for analysing data (V 0.1)

## Summary

1) Purpose of this script

2) What does the code do

3) How to use it

4) How to get the logs from your OAIBox

5) Contact in case somethings is wrong

6) License

### 1) Purpose of this script

To anyone who wants to use the OAIbox, you can in fact create your own script to parse the json file but here is one in case you want to use a CSV for analysing your data

you can see an exemple of result in **result_test.csv** from **log_test.json**

Be aware that if the format of OAIbox logs change, this script will then be depreciated


### 2) What does the code do

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
- Rssi
- Cqi
- Pucch Snr
- Pusch Snr

The script also delete line of logs with no Rnti (ue) inside.

### 3) How to use it

In the folder with the code and your logs.json file use this command:

```bash
python json_to_csv.py your-logs.json name-of-your-result-file.csv
```


### 4) How to get the logs of your OAIbox

- Go on the OAIbox dashboard

- Choose the Box that you want to collect the data

- Click on the NG-RAN icon (only if started)

- Then on the left of the dashboard click on the button to download the logs



### 5) Version

V 0.1 - 06/07/2023

### 6) License

This project is under the GNU GENERAL PUBLIC LICENSE-3.0 new or revised license. Please read the [LICENSE](LICENSE) file.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

