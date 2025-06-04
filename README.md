<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

</head>
<body>
    <h1>🛠️ NetCap: Basic Netcat-like Remote Shell in Python</h1>

    <p><strong>NetCap</strong> is a simple Python-based remote shell tool that mimics the behavior of Netcat. It allows a server to send shell commands to a client, and the client to execute them and send back the output using a TCP socket.</p>

    <hr />

    <h2>⚙️ How It Works</h2>

    <p>NetCap creates a basic socket connection using Python:</p>
    <ul>
        <li><code>AF_INET</code>: Defines we are using IPv4 addressing.</li>
        <li><code>SOCK_STREAM</code>: Specifies TCP protocol (connection-oriented).</li>
    </ul>

    <h3>Server Side (Listener)</h3>
    <ul>
        <li>Binds to an IP and port using <code>socket.bind()</code></li>
        <li>Listens for a connection using <code>socket.listen()</code></li>
        <li>Accepts a client using <code>socket.accept()</code></li>
        <li>Sends commands and receives output</li>
    </ul>

    <h3>Client Side (Agent)</h3>
    <ul>
        <li>Connects to the server using <code>socket.connect()</code></li>
        <li>Waits for command from the server</li>
        <li>Executes it using <code>subprocess.getoutput()</code></li>
        <li>Sends the result back</li>
    </ul>

    <hr />

    <h2>📦 Prerequisites</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Client and server should be on same network (or port forwarded if remote)</li>
        <li>Terminal access</li>
    </ul>

    <hr />

    <h2>🚀 Setup &amp; Usage</h2>

    <h3>🔹 Step 1: Clone the Repository</h3>
    <pre><code>git clone https://github.com/yourusername/netcap.git
cd netcap
</code></pre>

    <h3>🔹 Step 2: Run the Server</h3>
    <pre><code>python server.py
</code></pre>

    <p>You’ll see:</p>
    <pre><code>Listening for connections...
Connected to ('127.0.0.1', &lt;port&gt;)
</code></pre>

    <p>Now you can type shell commands like:</p>
    <pre><code>$ whoami
$ dir       # Windows
$ ls -l     # Linux/macOS
</code></pre>

    <h3>🔹 Step 3: Run the Client</h3>
    <pre><code>python client.py
</code></pre>

    <p>You’ll see:</p>
    <pre><code>Connected to server.
</code></pre>

    <p>It will silently wait for the server’s command and send back the results.</p>

    <hr />

    <h2>📁 File Structure</h2>
    <table border="1" cellpadding="5" cellspacing="0">
        <thead>
            <tr>
                <th>File</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>server.py</code></td>
                <td>Server side script to send commands</td>
            </tr>
            <tr>
                <td><code>client.py</code></td>
                <td>Client side script to receive and run commands</td>
            </tr>
            <tr>
                <td><code>README.md</code></td>
                <td>Project description and instructions</td>
            </tr>
            <tr>
                <td><code>.gitignore</code></td>
                <td>Ignores Python cache files and environment files</td>
            </tr>
            <tr>
                <td><code>LICENSE</code></td>
                <td>(Optional) MIT license for open-source use</td>
            </tr>
        </tbody>
    </table>

    <hr />

    <h2>✅ Supported Features</h2>
    <ul>
        <li>Remote command execution</li>
        <li>Bi-directional TCP communication</li>
        <li>Cross-platform (Windows/Linux)</li>
        <li>Small &amp; clean codebase (~30 lines each)</li>
    </ul>

    <hr />

    <h2>🔐 Warning &amp; Disclaimer</h2>
    <blockquote>
        <p>This tool is for <strong>educational and ethical penetration testing only</strong>.</p>
        <p>Do <strong>not</strong> use it on networks or systems without permission. Misuse of this tool may violate laws and policies.</p>
    </blockquote>

    <hr />

    <h2>🔄 Possible Enhancements</h2>
    <ul>
        <li>🔐 Add encryption using AES</li>
        <li>🧵 Add threading for multi-client support</li>
        <li>📂 Enable file transfer</li>
        <li>🧾 Logging of executed commands</li>
        <li>📡 Convert into a reverse shell (client initiates connect to server)</li>
    </ul>

    <hr />

    <h2>📜 License</h2>
    <p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>
</body>
</html>

