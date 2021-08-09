# from sslyze import (
#     ServerNetworkLocationViaDirectConnection,
#     ServerConnectivityTester,
#     Scanner,
#     ServerScanRequest,
#     ScanCommand,
# )
# from sslyze.errors import ConnectionToServerFailed


# def main() -> None:
#     # First validate that we can connect to the servers we want to scan
#     servers_to_scan = []
#     for hostname in ["www.codeforces.com"]:
#         server_location = ServerNetworkLocationViaDirectConnection.with_ip_address_lookup(hostname, 443)
#         try:
#             server_info = ServerConnectivityTester().perform(server_location)
#             servers_to_scan.append(server_info)
#         except ConnectionToServerFailed as e:
#             print(f"Error connecting to {server_location.hostname}:{server_location.port}: {e.error_message}")
#             return

#     scanner = Scanner()

#     # Then queue some scan commands for each server
#     for server_info in servers_to_scan:
#         server_scan_req = ServerScanRequest(
#             server_info=server_info, scan_commands={ScanCommand.CERTIFICATE_INFO, ScanCommand.SSL_2_0_CIPHER_SUITES},
#         )
#         scanner.queue_scan(server_scan_req)

#     # Then retrieve the result of the scan commands for each server
#     for server_scan_result in scanner.get_results():
#         print(f"\nResults for {server_scan_result.server_info.server_location.hostname}:")

#         # Scan commands that were run with no errors
#         try:
#             ssl2_result = server_scan_result.scan_commands_results[ScanCommand.SSL_2_0_CIPHER_SUITES]
#             print("\nAccepted cipher suites for SSL 2.0:")
#             for accepted_cipher_suite in ssl2_result.accepted_cipher_suites:
#                 print(f"* {accepted_cipher_suite.cipher_suite.name}")
#         except KeyError:
#             print("Encountered Error in ssl2 cipher suite scan")
#             pass

#         try:
#             certinfo_result = server_scan_result.scan_commands_results[ScanCommand.CERTIFICATE_INFO]
#             print("\nCertificate info:")
#             for cert_deployment in certinfo_result.certificate_deployments:
#                 print(f"Leaf certificate: \n{cert_deployment.received_certificate_chain_as_pem[0]}")
#         except KeyError:
#             print("Encountered Error in certificate information")
#             pass

#         try:
#             ccs_injection = server_scan_result.scan_commands_results[ScanCommand.HEARTBLEED]
#             print(temp)
#         #     print("\nOPENSSL_CCS_INJECTION:")
#         #     for x in temp:
#         #         print(x)
#         except KeyError:
#             print("HEARTBLEED_ERROR")
#             pass


#         # Scan commands that were run with errors
#         for scan_command, error in server_scan_result.scan_commands_errors.items():
#             print(f"\nError when running {scan_command}:\n{error.exception_trace}")


# if __name__ == "__main__":
#     main()


# def basic_example_connectivity_testing() -> None:
#     # Define the server that you want to scan
#     server_location = ServerNetworkLocationViaDirectConnection.with_ip_address_lookup("www.google.com", 443)

#     # Do connectivity testing to ensure SSLyze is able to connect
#     try:
#         server_info = ServerConnectivityTester().perform(server_location)
#     except ConnectionToServerFailed as e:
#         # Could not connect to the server; abort
#         print(f"Error connecting to {server_location}: {e.error_message}")
#         return
#     print(f"Connectivity testing completed: {server_info}")


# def basic_example() -> None:
#     # Define the server that you want to scan
#     server_location = ServerNetworkLocationViaDirectConnection.with_ip_address_lookup("www.google.com", 443)

#     # Do connectivity testing to ensure SSLyze is able to connect
#     try:
#         server_info = ServerConnectivityTester().perform(server_location)
#     except ConnectionToServerFailed as e:
#         # Could not connect to the server; abort
#         print(f"Error connecting to {server_location}: {e.error_message}")
#         return

#     # Then queue some scan commands for the server
#     scanner = Scanner()
#     server_scan_req = ServerScanRequest(
#         server_info=server_info, scan_commands={ScanCommand.CERTIFICATE_INFO, ScanCommand.SSL_2_0_CIPHER_SUITES},
#     )
#     scanner.queue_scan(server_scan_req)
  
#     # Then retrieve the results
#     for server_scan_result in scanner.get_results():
#         print(f"\nResults for {server_scan_result.server_info.server_location.hostname}:")

#         # SSL 2.0 results
#         ssl2_result = server_scan_result.scan_commands_results[ScanCommand.SSL_2_0_CIPHER_SUITES]
#         print("\nAccepted cipher suites for SSL 2.0:")
#         for accepted_cipher_suite in ssl2_result.accepted_cipher_suites:
#             print(f"* {accepted_cipher_suite.cipher_suite.name}")

#         # Certificate info results
#         certinfo_result = server_scan_result.scan_commands_results[ScanCommand.CERTIFICATE_INFO]
#         print("\nCertificate info:")
#         for cert_deployment in certinfo_result.certificate_deployments:
#             print(f"Leaf certificate: \n{cert_deployment.received_certificate_chain_as_pem[0]}")

import os
import subprocess
import sys
import json
def SSL_SCAN(ip_address):
    ip_address_out = ":".join(ip_address.split("."))
    f = open("/home/kali/Desktop/Final_Year_Project/cache/"+ip_address_out+"_ssl_check.json","w")
    outputfile_cache_ssl = open("/home/kali/Desktop/Final_Year_Project/cache/"+ip_address_out+"_ssl_output.txt","w")

    try:
        output = subprocess.Popen(["/usr/bin/sslyze","--regular","--json_out=/home/kali/Desktop/Final_Year_Project/cache/"+ip_address_out+"_ssl_check.json",ip_address],stdout=subprocess.PIPE,universal_newlines=True)
        #continue
        f.close()
        print(output.stdout.read())
        #json_output = json.load(f.read())
        f = open("/home/kali/Desktop/Final_Year_Project/cache/"+ip_address_out+"_ssl_check.json","r")

        json_output = json.load(f)
        outputfile_cache_ssl.write("SSL SECURITY TESTING - WEB APPLICATION of "+ip_address+"\n")
        outputfile_cache_ssl.write("SCAN COMMANDS USED: \n")
        outputfile_cache_ssl.writelines("%s \n" % l for l in json_output["server_scan_results"][0]["scan_commands"])
        outputfile_cache_ssl.write("\n HEARTBLEED VULN: \n")
        outputfile_cache_ssl.write(str(json_output["server_scan_results"][0]["scan_commands_results"]["heartbleed"]["is_vulnerable_to_heartbleed"]))
        outputfile_cache_ssl.write("\n OPENSSL CCS INJECTION VULN: \n")
        outputfile_cache_ssl.write(str(json_output["server_scan_results"][0]["scan_commands_results"]["openssl_ccs_injection"]["is_vulnerable_to_ccs_injection"]))
        outputfile_cache_ssl.write("\n ROBOT VULN: \n")
        outputfile_cache_ssl.write(json_output["server_scan_results"][0]["scan_commands_results"]["robot"]["robot_result"])
        
        outputfile_cache_ssl.write("\n SSL 2.0 probing results:")
        outputfile_cache_ssl.write("\n Accepted ciphers:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["ssl_2_0_cipher_suites"]["accepted_cipher_suites"])))
        outputfile_cache_ssl.write("\n Rejected cipher suites:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["ssl_2_0_cipher_suites"]["rejected_cipher_suites"])))
        
        outputfile_cache_ssl.write("\n SSL 3.0 probing results:")
        outputfile_cache_ssl.write("\n Accepted ciphers:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["ssl_3_0_cipher_suites"]["accepted_cipher_suites"])))
        outputfile_cache_ssl.write("\n Rejected cipher suites:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["ssl_3_0_cipher_suites"]["rejected_cipher_suites"])))
        
        outputfile_cache_ssl.write("\n TLS1.0 probing results:")
        outputfile_cache_ssl.write("\n Accepted ciphers:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["tls_1_0_cipher_suites"]["accepted_cipher_suites"])))
        outputfile_cache_ssl.write("\n Rejected cipher suites:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["tls_1_0_cipher_suites"]["rejected_cipher_suites"])))
        
        outputfile_cache_ssl.write("\n TLS1.1 probing results:")
        outputfile_cache_ssl.write("\n Accepted ciphers:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["tls_1_1_cipher_suites"]["accepted_cipher_suites"])))
        outputfile_cache_ssl.write("\n Rejected cipher suites:")    
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["tls_1_1_cipher_suites"]["rejected_cipher_suites"])))
        
        outputfile_cache_ssl.write("\n TLS1.2 probing results:")
        outputfile_cache_ssl.write("\n Accepted ciphers:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["tls_1_2_cipher_suites"]["accepted_cipher_suites"])))
        outputfile_cache_ssl.write("\n Rejected cipher suites:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["tls_1_2_cipher_suites"]["rejected_cipher_suites"])))
        
        outputfile_cache_ssl.write("\n TLS1.3 probing results:")
        outputfile_cache_ssl.write("\n Accepted ciphers:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["tls_1_3_cipher_suites"]["accepted_cipher_suites"])))
        outputfile_cache_ssl.write("\n Rejected cipher suites:")
        outputfile_cache_ssl.write(str(len(json_output["server_scan_results"][0]["scan_commands_results"]["tls_1_3_cipher_suites"]["rejected_cipher_suites"])))
        
        outputfile_cache_ssl.write("\n RESULT:")
        outputfile_cache_ssl.write("\n cipher suite supported:" + json_output["server_scan_results"][0]["server_info"]["tls_probing_result"]["cipher_suite_supported"])
        outputfile_cache_ssl.write("\n client auth requirement:" + json_output["server_scan_results"][0]["server_info"]["tls_probing_result"]["client_auth_requirement"])
        outputfile_cache_ssl.write("\n highest tls version supported:" + json_output["server_scan_results"][0]["server_info"]["tls_probing_result"]["highest_tls_version_supported"])

        outputfile_cache_ssl.write("\n CURRENT STABLE TLS VERSION IN INTERNET IS TLS 1.2 or 1.3 - anything below that is deprecated and prone to attacks \n")
        outputfile_cache_ssl.write("for more details perform a manual scan using: sslyze --regular " + ip_address)
        #outputfile_cache_ssl.close()
        f.close()
        print("Generated temp report")
    
    except:

        print("error generating report. please perform a manual scan using: sslyze --regular " + ip_address)
    finally:
        outputfile_cache_ssl.close()

    return ip_address_out+"_ssl_output.txt"
    






    # outputfile_cache_ssl.write("SSLYZE - scans performed are: \n" + json_output["scan_commands"])
    # if json_output["scan_commands_errors"].keys() == 0:
    #     outputfile_cache_ssl.write("\n There was an error in scan. Please perform a manual scan with sslyze!")
    #     print("SSLYZE SCAN COMPLETED")
    #     return
    # outputfile_cache_ssl.write("RECEIVED CERTIFICATE CHAIN: \n")
    # outputfile_cache_ssl.write(json_output["received_certificate_chain"][0]["as_pem"])


if __name__ == "__main__":
    SSL_SCAN(sys.argv[1])