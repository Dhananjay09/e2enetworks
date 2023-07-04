from e2enetworks.cloud import tir
from e2enetworks.cloud.tir import PipelineClient

token="eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGSjg2R2NGM2pUYk5MT2NvNE52WmtVQ0lVbWZZQ3FvcXRPUWVNZmJoTmxFIn0.eyJleHAiOjE3MTk1OTQyNzQsImlhdCI6MTY4ODA1ODI3NCwianRpIjoiMDJlYmI0NGMtYWM5NC00Nzg4LTk0NDItOGI0ZjE4NGE1N2Q4IiwiaXNzIjoiaHR0cDovLzE3Mi4xNi4yMzEuMTM6ODA4MC9hdXRoL3JlYWxtcy9hcGltYW4iLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMDcwNGUyYTktM2RlZC00NjQyLWI1M2MtMjA1OTJiNDU5MzdlIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYXBpbWFudWkiLCJzZXNzaW9uX3N0YXRlIjoiYmI2NGUwMWYtN2I0Ny00MTcyLWFlNDItYzBkZmVjNmE3NTI0IiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwOi8vMTcyLjE2LjIzMS4xMzo4MDgwIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiYXBpdXNlciIsImRlZmF1bHQtcm9sZXMtYXBpbWFuIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiYmI2NGUwMWYtN2I0Ny00MTcyLWFlNDItYzBkZmVjNmE3NTI0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoic2hpdmFuc2ggamFpbiIsInByZWZlcnJlZF91c2VybmFtZSI6InNoaXZhbnNoLmphaW4rdGhvcnRlc3RAZTJlbmV0d29ya3MuY29tIiwiZ2l2ZW5fbmFtZSI6InNoaXZhbnNoIiwiZmFtaWx5X25hbWUiOiJqYWluIiwiZW1haWwiOiJzaGl2YW5zaC5qYWluK3Rob3J0ZXN0QGUyZW5ldHdvcmtzLmNvbSJ9.Ibrs4LTP5pcMf3voP5ZFThuh4pnqCq5I0BvX19XAiGkFWI3D1gRMgSH4jKHjx9BnQz1Tlm9fYbD_5koJgjySTTZFQetImotMdS1-4xgHqX2ghRBmS2_9q6CRm8EVM1xZzs4XsU16d-VuF2tHqEWQCFNxKoEUfzoWG-eTz4hSA8Q"

def test_init():
    print(f'Start test') 
    tir.init(api_key="test", access_token=token, project="578")
    
    p = PipelineClient()
    response = p.list_pipelines()
    print(response.content)

def test_list():
    tir.init(api_key="test", access_token=token, project="578")
    
    p = PipelineClient()
    response = p.list_experiments()
    print("list_experiments:")
    print(response.content)

def test_experiment():
    tir.init(api_key="test", access_token=token, project="578")
    
    p = PipelineClient()
    print(p.create_experiment(name="test", description="test exp"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_list()

