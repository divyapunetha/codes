import java.io.BufferedReader;
import java.io.InoutStreamReader;
import java.io.PrintWriter;
import java.io.ServerSocket;
import java.io.Socket;
public class WebServer
	protected void start() {
		SereverSocket s;
		System.out.println("webserver starting");
		try{
			s = new ServerSocket(80);
		} catch(Exception e) {
			System.out.println("Error. Server not created")
			return;
		}
		System.out.println("waiting for response");
		for(;;) {
			try{
				Socket remote = s.accept(); // remote is now the connected socket
				System.out.println("connection,sending data");
				BufferedReader in = new BufferedReader(remote.getInputStream()));
				PrintWriter out = new PrintWriter(remote.getOutputStream());
				String str = ".";
				while(!str.equals(""))
					str = in.readLine();
				//Send the response
				out.println("HTTP/1.0 200 OK");
				out.println("Content-Type:text/html");
				out.printtln("<H1> WELCOME </H1>")
				out.flush();
				remote.close();
			} catch (Exception e) {
				System.out.println("Error. no connection");
				}
			}
		}
public static void main(String arg[]) {
	WebServer ws = new WebServer();
	ws.start();
	}
}
