This repository contains a number of python programs some with their respective questions and some without explanation if you find it difficult to understand then just drop a comment to let me know. Hope you find what you are looking for!




using Microsoft.Azure.Storage.Auth.StorageCredentials;
using Microsoft.Azure.Storage.CloudStorageAccount;
using Microsoft.Azure.Storage.Blob.CloudBlobClient;
using Microsoft.Azure.Storage.Blob.CloudBlobContainer;
using Microsoft.Azure.Storage.Blob.CloudBlobDirectory;

using System.IO.Stream;

public final class FetchDataFromBlobStorage
{
    public static void main(Args _args)
    {
        // Passing the connection string and storage account name
        Microsoft.Azure.Storage.Auth.StorageCredentials storageCredentials = new Microsoft.Azure.Storage.Auth.StorageCredentials("aofinancetest", "ORmQejJLdvFaYJnoqXB8pzFke0txsEWQ1zdxA6KvEEDcsu5u7xI2y5EJrjEMY+3iT/oweaekg1mY+AStWFbWMw==");

        // Using above credentials we instantiate a storage account and the object represents a storage account in azure
        Microsoft.Azure.Storage.CloudStorageAccount cloudStorageAccount = new Microsoft.Azure.Storage.CloudStorageAccount(storageCredentials, true);

        // To access the blob storage we extablish a client side interface
        Microsoft.Azure.Storage.Blob.CloudBlobClient cloudBlobClient =  new Microsoft.Azure.Storage.Blob.CloudBlobClient(cloudStorageAccount.BlobStorageUri, storageCredentials, null);

        // Limiting our search to a single container
        Microsoft.Azure.Storage.Blob.CloudBlobContainer cloudBlobContainer = cloudBlobClient.GetContainerReference("purchase-invoice");

        Microsoft.Azure.Storage.Blob.CloudBlobDirectory cloudBlobDirectory = cloudBlobContainer.GetDirectoryReference("Inbound");

        // Searching blobs in a particular directory of the container
        var listOfBlobs = cloudBlobDirectory.ListBlobs(true, 0, null, null);

        // Passing Flat listing as true so all blobs are retrived
        //var listOfBlobs = cloudBlobContainer.ListBlobs(null, true, 0, null, null);

        // Creating an enumerator to ietrate over each blob in the container
        var enumerator = listOfBlobs.GetEnumerator();

        while(enumerator.MoveNext())
        {
            // Each element of the enumerator is a Block blob because we have flat listing enabled
            Microsoft.Azure.Storage.Blob.CloudBlockBlob cloudBlockBlob = enumerator.get_current();

            // Checking blob tier to skip archived blobs
            str blobTier = cloudBlockBlob.Properties.StandardBlobTier.ToString();
            
            if(blobTier != "Archive")
            {
                // Memory stream object to download data from blob
                System.IO.MemoryStream memStream = new System.IO.MemoryStream();

                // Downloading the blob content into a memory stream
                cloudBlockBlob.DownloadToStream(memStream, null, null, null);

                // Pulling the cursor to the begining of the stream
                memStream.Seek(0, System.IO.SeekOrigin::Begin);

                // Reader object to read from the memory stream
                System.IO.StreamReader reader = new System.IO.StreamReader(memStream);

                // Reads all the content of the blob from start to end
                str blobContent = reader.ReadToEnd();

                Info(strFmt("Blob Name: %1, Blob Tier: %2 Blob Content: %3", cloudBlockBlob.Name, blobTier, blobContent));
                
                // If you want to reuse the same object then you can use this
                memStream.SetLength(0);

                // If you want to dispose the object itself and create a new one in the next loop
                memStream.Dispose();
            
            }

            

        }

    }

}
