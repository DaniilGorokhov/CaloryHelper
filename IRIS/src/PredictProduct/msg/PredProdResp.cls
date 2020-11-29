Class PredictProduct.msg.PredProdResp Extends (%Persistent, Ens.Response)
{

Property Matches As %String;

Storage Default
{
<Data name="MatchesDefaultData">
<Subscript>"PredProdResp"</Subscript>
<Value name="1">
<Value>Matches</Value>
</Value>
<Value name="2">
<Value>%%CLASSNAME</Value>
</Value>
</Data>
<DataLocation>^PredictProducF96A.PredProdRespD</DataLocation>
<DefaultData>MatchesDefaultData</DefaultData>
<IdLocation>^PredictProducF96A.PredProdRespD</IdLocation>
<IndexLocation>^PredictProducF96A.PredProdRespI</IndexLocation>
<StreamLocation>^PredictProducF96A.PredProdRespS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
