# Screenly OSE -- Digital Signage for the Raspberry Pi

This branch has the following modifications:
* &lt;macaddr&gt;, &lt;ipaddr&gt; and &lt;hostname&gt; tags in stored URIs are replaced when used, so that a cloned rpi disk image can automatically distinguish itself to a web server.
* Duration of the splash screen is configurable in screenly.conf with [viewer] setting splash_time = <i>nnn</i>
   

To learn more about Screenly, please visit the official website at [ScreenlyApp.com](http://www.screenlyapp.com). On the official site, you'll find the complete installation instructions, along with a live-demo of Screenly.

### Running the Unit Tests

    nosetests --with-doctest

