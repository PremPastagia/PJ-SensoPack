from api.index import predict, PredictRequest
import json
import os

os.environ['FIREBASE_URL'] = 'https://pj-sensopack-default-rtdb.asia-southeast1.firebasedatabase.app/'

req = PredictRequest(ph_level=7.0, storage_time_hrs=24.0)

try:
    print(predict(req))
except Exception as e:
    import traceback
    traceback.print_exc()
