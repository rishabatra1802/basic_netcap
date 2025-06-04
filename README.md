<!DOCTYPE html>
<html>

<body>
  <h1>🛠️ NetCap: Basic Netcat-like Remote Shell in Python</h1>

  <h2>Overview</h2>
  <p><strong>NetCap</strong> is a simple Python-based remote shell tool that mimics the behavior of Netcat. It allows a server to send shell commands to a client, which executes them and returns the output using a TCP socket connection.</p>

  <h2>Features</h2>
  <ul>
    <li>Creates TCP socket connection using <code>AF_INET</code> (IPv4) and <code>SOCK_STREAM</code> (TCP).</li>
    <li>Server listens and accepts connections from clients.</li>
    <li>Client receives commands, executes them via <code>subprocess.getoutput()</code>, and sends back results.</li>
    <li>Supports remote command execution on Windows/Linux platforms.</li>
  </ul>

  <h2>Getting Started</h2>
  <ol>
    <li>Clone the repository:</li>
  </ol>
  <pre><code>git clone https://github.com/yourusername/netcap.git</code></pre>

  <ol start="2">
    <li>Navigate to the project directory:</li>
  </ol>
  <pre><code>cd netcap</code></pre>

  <ol start="3">
    <li>Run the server script:</li>
  </ol>
  <pre><code>python server.py</code></pre>

  <p>The server will start listening for connections:</p>
  <pre><code>Listening for connections...
Connected to ('127.0.0.1', &lt;port&gt;)</code></pre>

  <ol start="4">
    <li>Run the client script on the same machine or another reachable machine:</li>
  </ol>
  <pre><code>python client.py</code></pre>

  <p>The client will connect and wait for commands silently.</p>

  <h2>Usage</h2>
  <ul>
    <li>Type commands in the server terminal prompt to execute remotely on the client.</li>
    <li>Examples:</li>
  </ul>
  <pre><code>$ whoami
$ dir    # Windows
$ ls -l  # Linux/macOS
</code></pre>

  <h2>File Structure</h2>
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
        <td>Server-side script to send commands</td>
      </tr>
      <tr>
        <td><code>client.py</code></td>
        <td>Client-side script to receive and execute commands</td>
      </tr>
      <tr>
        <td><code>README.md</code></td>
        <td>Project documentation</td>
      </tr>
      <tr>
        <td><code>.gitignore</code></td>
        <td>Ignore Python cache and environment files</td>
      </tr>
      <tr>
        <td><code>LICENSE</code></td>
        <td>MIT License file (optional)</td>
      </tr>
    </tbody>
  </table>

  <h2>Warning &amp; Disclaimer</h2>
  <p><strong>Use this tool only for educational and authorized penetration testing purposes.</strong> Unauthorized use on networks or systems is illegal and unethical.</p>

  <h2>Possible Enhancements</h2>
  <ul>
    <li>Add AES encryption for secure communication</li>
    <li>Implement threading to support multiple clients</li>
    <li>Enable file transfer functionality</li>
    <li>Log executed commands for audit purposes</li>
    <li>Convert to reverse shell where client initiates connection</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>

</body>
</html>
