Class PredictProduct.PredictProdProcess Extends (Ens.BusinessProcessBPL, isc.py.ens.ProcessUtils) [ DependsOn = isc.py.ens.ProcessUtils ]
{

/// Python Operation we use to execute Python code
Property PythonOperation As %String(MAXLEN = 128) [ InitialExpression = "isc.py.ens.Operation" ];

Parameter SETTINGS = "PythonOperation:ML:selector?context={Ens.ContextSearch/ProductionItems?targets=1&productionName=@productionId}";

/// BPL Definition
XData BPL [ XMLNamespace = "http://www.intersystems.com/bpl" ]
{
<process language='objectscript' request='PredictProduct.msg.PredProdReq' response='PredictProduct.msg.PredProdResp' >
<sequence >

<call name='Predict product name' target='@..%Process.PythonOperation' async='1'>
<annotation><![CDATA[
from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "#{process.%request.Target.Filename}"), result_count=10)

result = ""

for eachPrediction, eachProbability in zip(predictions, probabilities):
    result += eachPrediction + ":" + eachProbability + ";"

]]></annotation>
<request type='isc.py.msg.ExecutionRequest' >
<assign property="callrequest.Code" value='process.GetAnnotation("Predict product name")' action="set" />
<assign property="callrequest.Variables" value='"result"' action="set" />
<assign property="callrequest.Serialization" value='"JSON"' action="set" />
<assign property="callrequest.SeparateLines" value="0" action="set" />
</request>
<response type='isc.py.msg.ExecutionResponse'>
<assign property="context.matches" value='callresponse.Variables.GetAt("result")' action="set" />
</response>
</call>
<sync name='Wait for Predict product name' calls='Predict product name' type='all' />

<assign name="Fill Response" property="status" value="process.FillResponse()"/>


</sequence>
</process>
}

Method FillResponse() As %Status
{
	#dim sc As %Status = $$$OK

	do ..%response.Matches.SetAt("result", ..%Context.matches)
	
	quit sc
}

Storage Default
{
<Data name="PredictProdProcessDefaultData">
<Subscript>"PredictProdProcess"</Subscript>
<Value name="1">
<Value>PythonOperation</Value>
</Value>
<Value name="2">
<Value>Width</Value>
</Value>
<Value name="3">
<Value>Height</Value>
</Value>
</Data>
<DefaultData>PredictProdProcessDefaultData</DefaultData>
<Type>%Storage.Persistent</Type>
}

}
