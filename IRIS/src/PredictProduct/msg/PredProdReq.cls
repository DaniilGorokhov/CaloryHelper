Class PredictProduct.msg.PredProdReq Extends (%Persistent, Ens.Request)
{

/// Target photo
Property Target As PredictProduct.data.Photo [ Required ];

Storage Default
{
<Data name="PredProdReq">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>MatchesVariable</Value>
</Value>
<Value name="3">
<Value>TargetId</Value>
</Value>
<Value name="4">
<Value>TargetPhoto</Value>
</Value>
<Value name="5">
<Value>Target</Value>
</Value>
</Data>
<DataLocation>^PredictProduct.msg.PredProdReqD</DataLocation>
<DefaultData>PredProdReqDefaultData</DefaultData>
<IdLocation>^PredictProduct.msg.PredProdReqD</IdLocation>
<IndexLocation>^PredictProduct.msg.PredProdReqI</IndexLocation>
<StreamLocation>^PredictProduct.msg.PredProdReqS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
