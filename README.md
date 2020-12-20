# heating system alarm

I've created a Heating-Alert system. It mesures the Temperature in the Heating-sytem in my House. 
The idea came to me after several heating failures. 
The heating system has its own built-in alarm system, but this has never worked properly. That's why I built my own small system here. 

## How it works
A DHT22 sensor is used to measure the temperature at the water pipe. However, this is somewhat lower than the real value. That is why there is an offset in the script. 
This data is then fed into a database. From there it will be processed and optically processed with the help of Grafana.

In the event of a temperature drop below 63 degrees Celsius, an alarm is sent by e-mail.

## Install 
Download the full Git-Repo to your Raspberry-Pi.

```sh
git clone https://github.com/julianbruegger/heating-system-alarm.git
```

The requirements.txt must be executed for the installation. 
```sh
pip install -r requirements.txt
```

After that create a [cronjob](https://crontab-generator.org/) for your sensor-script.  
