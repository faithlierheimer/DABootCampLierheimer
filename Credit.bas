Attribute VB_Name = "Module1"
Sub Credit()
Dim lastrow As Long
Dim amexcounter As Integer
Dim bankcardcounter As Integer
Dim amexcharges As Integer
Dim bankcardcharges As Integer
lastrow = Cells(Rows.Count, 1).End(xlUp).Row
amexcounter = 0
amexcharges = 0
bankcardcounter = 0
bankcardcharges = 0

For i = 2 To lastrow
    If Cells(i, 1).Value = "americanexpress" Then
    amexcounter = amexcounter + 1
    amexcharges = amexcharges + Cells(i, 3).Value
    ElseIf Cells(i, 1).Value = "bankcard" Then
    bankcardcounter = 0
    bankcardcharges = bankcardcharges + Cells(i, 3).Value
    End If
Next i
Cells(2, 5).Value = bankcardcharges
Cells(2, 6).Value = amexcharges

End Sub
