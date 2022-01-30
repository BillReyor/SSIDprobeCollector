# SSIDprobeCollector
An ML &amp; Correlation platform for transforming disparate data points of interest into usable intelligence.

At a High level the platform will do the following in its most basic operational state:
1. Collect SSID Probes against a timeline and location
2. Collect video or photo against a timeline and location
3. Diff the probe requests typical for the location with those at the moment of capture
4. Log multiple times where ML is certain the subject is the same (and unique) storing the result
5. Where Unique probe requests are identified perform an API lookup on https://www.wigle.net and store SSID,Photo & and map result
6. If Wigle lookup fails just store the correlated data.
