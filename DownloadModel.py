
from google.cloud import storage

Bucket_Name = "aiesg-cpt-data"

key_path = 'key.json'
storage_client = storage.Client.from_service_account_json(key_path)
bucket = storage_client.get_bucket(Bucket_Name)

Cloud_Filename = 'CPT_demo_2_378k_i0.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i1.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i2.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i3.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i4.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i5.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i6.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i7.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i8.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i9.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i10.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i11.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

Cloud_Filename = 'CPT_demo_2_378k_i12.h5'
blob = bucket.blob(Cloud_Filename)
blob.download_to_filename(Cloud_Filename)

storage_client.close()
