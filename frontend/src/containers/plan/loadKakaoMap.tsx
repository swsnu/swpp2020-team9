function loadKakaoMap(callback: any) {
  const existingScript = document.getElementById("kakaoMap");

  if (!existingScript) {
    const script = document.createElement("script");
    script.src =
      "//dapi.kakao.com/v2/maps/sdk.js?appkey=7597dfaa5a206594137f73cc7a8ebcdd";
    script.id = "kakaoMap";

    document.body.appendChild(script);

    script.onload = () => {
      if (callback) {
        callback();
      }
    };
  }
  if (existingScript && callback) {
    callback();
  }
}

export default loadKakaoMap;
