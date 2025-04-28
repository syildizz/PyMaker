from typing import Iterable
import http.client
from http.client import HTTPResponse
import json
from config import pymaker_config, get_prompt_prefix

def make_prompt_request(prompt: str) -> int | Iterable[dict[str, str]]:
    response = _make_prompt_request(prompt)
    if response.status != 200:
        return response.status
    else:
        return _read_prompt_response_stream(response)

def _make_prompt_request(prompt: str):
    conn = http.client.HTTPConnection(pymaker_config["ollama_host_ip"], pymaker_config["ollama_host_port"])
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
    }
    conn.request(
        'POST',
        '/api/generate',
        f'{{"model":"{pymaker_config["ollama_model"]}","prompt":"{_process_prompt_for_ollama(prompt)}"}}'.encode("utf-8"),
        headers
    )
    response = conn.getresponse()
    return response

def _read_prompt_response_stream(response: HTTPResponse) -> Iterable[dict[str, str]]:
    while chunk := response.readline():
        yield json.loads(chunk)

def _process_prompt_for_ollama(prompt: str) -> str:
    return prompt.replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r")

if __name__=="__main__":
    acc: str = ""
    maybe_response_stream = make_prompt_request(get_prompt_prefix() + "Reverse a listboom")
    if isinstance(maybe_response_stream, int):
        status_code = maybe_response_stream
        print(f"Error: Ollama failed to respond with status code {status_code}.")
    else:
        response_stream = maybe_response_stream
        for chunk in response_stream:
            acc += chunk["response"] #type: ignore
            print(repr(chunk))
        print(acc)
