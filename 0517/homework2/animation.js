function clickOrder() {
    //이름
    let orderName = $('#order-name').val();
    //수량
    let orderCnt = $('#order-cnt').val();

    //주소
    let orderAddress = $('#order-address').val();

    //전화번호
    let orderTel = $('#order-tel').val();

    /*
    //리스트를 이용하여. (좋은방법임)
    let inputBox=[
        ['이름', $('#order-name').val()],
        ['수량', $('#order-cnt').val()]
    ]
     */

    //다시 코드를 수정해보자.
    //이름요소가 비어있다면
    let error = "";
    if (orderName == "") {
        alert("이름을 입력해주세요!\n");
    }

    //수량이 비어있다면
    if (orderCnt == "-- 수량을 선택해주세요 --") {
        error=error.concat("수량을 선택해주세요!\n");
    }

    //주소
    if (orderAddress == '') {
        error=error.concat("주소를 입력해주세요!\n");
    }

    //전화번호
    if (orderTel == '') {
        error=error.concat("전화번호를 입력해주세요!\n");
    }

    console.log(error);
    console.long(error.length)
    // 입력요소중 하나라도 비어있다면
    if (error == '') {
        let orderSuccess = `${orderName}님 주문하신 제품 ${orderCnt}개 주문완료했습니다.\n배달이 시작되면 ${orderTel} 로 문자 전송하겠습니다.`
        alert(orderSuccess);
    } else {
        alert(error);
    }
}