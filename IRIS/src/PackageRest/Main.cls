Include Ensemble

Class PackageRest.Main Extends %CSP.REST
{

Parameter HandleCorsRequest = 1;

XData UrlMap [ XMLNamespace = "http://www.intersystems.com/urlmap" ]
{
<Routes>
    <Route Url="/product_name" Method="POST" Call="productName"/>
    <Route Url="/test" Method="GET" Call="test"/>
</Routes>
}

ClassMethod productName() As %Status
{
    #dim %request As %CSP.Request	
	#dim stream As %CSP.BinaryStream
	set stream = %request.GetMimeData("file")

	set ext = $ZCVT($select(stream.FileName[".":$piece(stream.FileName,".",*),1:""),"l")
	set file = ##class(%File).TempFilename(ext)
	set fileStream = ##class(%Stream.FileBinary).%New()
	do fileStream.LinkToFile(file)
	set sc = fileStream.CopyFromAndSave(stream)
	quit:$$$ISERR(sc) sc
	
	set photo = ##class(PredictProduct.data.Photo).%New()
	set photo.Data = fileStream
	set sc = photo.%Save()
	quit:$$$ISERR(sc) sc
	
	set timeout = 60
	set processName = "PredictProduct.PredictProdProcess"
	set serviceName = "EnsLib.Testing.Service"
	
	set req = ##class(PredictProduct.msg.PredProdReq).%New()
	
	set req.Target = photo
	
	set sc = ..InvokeHostSync(processName, req, .resp, timeout, serviceName)
	quit:$$$ISERR(sc) sc
	quit:'$isObject(resp) $$$ERROR($$$GeneralError, "Timeout")
	
	#dim resp As PredictProduct.msg.PredProdResp
    set httpResp = {}

    do httpResp.%Set("result", resp.Matches)
	
	set %response.ContentType = ..#CONTENTTYPEJSON
	write httpResp.%ToJSON()
	
	quit sc
}

ClassMethod InvokeHostSync(targetHostName As %String, request As %Persistent, Output response As %Persistent, timeout As %Integer, serviceName As %String = "EnsLib.Testing.Service")
{
	#dim sc As %Status
		
	#dim service As Ens.BusinessService
	set sc = ##class(Ens.Director).CreateBusinessService(serviceName, .service)
	quit:$$$ISERR(sc) sc
	set sc = service.SendRequestSync(targetHostName, request, .response, timeout)
	
	quit sc
}

ClassMethod test() As %Status
{
	set sc = "1, 2, 3"

    write sc

    quit 1
}

}
