from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello_world():
    return '''
<div>
    <div>
        <li class="basicList_item__0T9JD ad">
            <div class="basicList_inner__xCM3J">
                <div class="basicList_img_area__AdRY_">
                    <div class="thumbnail_thumb_wrap__RbcYO _wrapper"><a target="_blank" class="thumbnail_thumb__Bxb6Z"
                            rel="noopener" data-nclick="N=a:lst*A.image,r:1,i:85050028140"
                            data-testid="SEARCH_PRODUCT_AD"
                            href="https://adcr.naver.com/adcr?x=pWXquo+6HIn6Vhh8oER1QP///w==kA6Fn1FQzMP2q8RN3peUFDrf/AFh7R/LnY2itBKt3P8x+wJqHD7kAUDpP7gjTCPMq6cSxPo0lvZQQstDt9SdR8LVFNVoJ5GMdANVhfH1avLulmWsVXTmBdJE6KZ6S8ujrwX1kNqhMhb66guU7GrOaXomdtnEK2iMCs7ON9BM+lbQbsccMz3bKRzlg1bowmf5bBexDIrreIG+QlmxMgr4Za1ZzAOxUloGnIpnW3JfsDBUol1502mJl6t4gugNXJs8Pq5IQZb7d1m3+xPUMIbtKAsQzm3fSaYY4VjPl4np4QepsicvcYmUMlfm4a12+HgZ/eYjHVGZgRRZ0B+uHO3thAgSpoGqj2KKHov9jYExOfkHXg1TzT6Hh8+EAX5gWwikR2jlFUYVferMBwMElCvUDo/CK/Kf7blrh1HHnoMTpC8xdm+q5F5/v/CXrtj2HoV5e+311hK1evJHF1h32OPIfXvFuVN5SATvn1roC4uInZ0vlI1e85ymf8vAGpa/Efm7DBzQWZEV7Xnab3kxdRlzZG5qa4WYfjH+h6BIZSNO5vGanyAid8DxpmJtJ62pOoErm3O+Kh0IpXOTVoZSYp+clxqH78G6Ognsg04ogGmMv+sBMnHI2Vj6sabI03/vr4dxRyBH4/lmqj7sSPbDloO0x5qbELGYmo+W1D7uuIWrPOnpYX0GX9gtMzyTvQbJtL+QvjbpdIs5QH0yLpEJOz261a1xHT3BePpK+i/u7bQMFIWWAs7Eam3PK6xngyUSOK7EnjTmqpd3mOZ6TvLKCUCUy6gbWdlrBRwwKQ1c0hPyaCZ60txd662SznsojDkEH++bUus/r6c+3t0TJAaE/j3Tft8Psv4JFbceJCEzcoSFiMTBS0yktkiX2hUfFcyMC2O78M9xdzehJLchi9bHPJYvyGhwsJHYIggaThTbbcz+rx5g="><img
                                width="140" height="140" alt="스팸클래식 200Gx20개 (1박스)"
                                src="https://shopping-phinf.pstatic.net/main_8505002/85050028140.jpg?type=f140"></a>
                        <div class="thumbnail_btn_box____IiP">
                            <div class="thumbnail_btn__3Gjg1"><button type="button" class="thumbnail_save__yu3R_"
                                    data-nclick="N=a:lst*A.put"><span
                                        class="thumbnail_layer_info__r_5dH">담기</span></button>
                                <div class="thumbnail_layer_info__r_5dH">
                                    <div class="thumbnail_link_box__fhsB8"><a href="#" class="thumbnail_link__i3ShY"
                                            data-nclick="N=a:lst*A.putblog">내 블로그에 담기</a><a href="#"
                                            class="thumbnail_link__i3ShY" data-nclick="N=a:lst*A.putcafe">카페에 담기</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="basicList_info_area__TWvzp">
                    <div class="basicList_title__VfX3c"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*A.title,i:85050028140,r:1" data-testid="SEARCH_PRODUCT_AD"
                            title="스팸클래식 200Gx20개 (1박스)"
                            href="https://adcr.naver.com/adcr?x=pWXquo+6HIn6Vhh8oER1QP///w==kA6Fn1FQzMP2q8RN3peUFDrf/AFh7R/LnY2itBKt3P8x+wJqHD7kAUDpP7gjTCPMq6cSxPo0lvZQQstDt9SdR8LVFNVoJ5GMdANVhfH1avLulmWsVXTmBdJE6KZ6S8ujrwX1kNqhMhb66guU7GrOaXomdtnEK2iMCs7ON9BM+lbQbsccMz3bKRzlg1bowmf5bBexDIrreIG+QlmxMgr4Za1ZzAOxUloGnIpnW3JfsDBUol1502mJl6t4gugNXJs8Pq5IQZb7d1m3+xPUMIbtKAsQzm3fSaYY4VjPl4np4QepsicvcYmUMlfm4a12+HgZ/eYjHVGZgRRZ0B+uHO3thAgSpoGqj2KKHov9jYExOfkHXg1TzT6Hh8+EAX5gWwikR2jlFUYVferMBwMElCvUDo/CK/Kf7blrh1HHnoMTpC8xdm+q5F5/v/CXrtj2HoV5e+311hK1evJHF1h32OPIfXvFuVN5SATvn1roC4uInZ0vlI1e85ymf8vAGpa/Efm7DBzQWZEV7Xnab3kxdRlzZG5qa4WYfjH+h6BIZSNO5vGanyAid8DxpmJtJ62pOoErm3O+Kh0IpXOTVoZSYp+clxqH78G6Ognsg04ogGmMv+sBMnHI2Vj6sabI03/vr4dxRyBH4/lmqj7sSPbDloO0x5qbELGYmo+W1D7uuIWrPOnpYX0GX9gtMzyTvQbJtL+QvjbpdIs5QH0yLpEJOz261a1xHT3BePpK+i/u7bQMFIWWAs7Eam3PK6xngyUSOK7EnjTmqpd3mOZ6TvLKCUCUy6gbWdlrBRwwKQ1c0hPyaCZ60txd662SznsojDkEH++bUus/r6c+3t0TJAaE/j3Tft8Psv4JFbceJCEzcoSFiMTBS0yktkiX2hUfFcyMC2O78M9xdzehJLchi9bHPJYvyGhwsJHYIggaThTbbcz+rx5g=">스팸클래식
                            200Gx20개 (1박스)</a></div>
                    <div class="basicList_price_area__K7DDT"><button type="button"
                            class="ad_ad_stk__pBe5A">광고</button><strong class="basicList_price__euNoD"><span><span
                                    class="price_num__S2p_v" data-testid="SEARCH_PRODUCT_PRICE">52,890원</span><span
                                    class="price_delivery__yw_We"><svg width="15" height="12" fill="none"
                                        xmlns="http://www.w3.org/2000/svg" class="price_svg_delivery__kOiSU">
                                        <mask id="IconProductDelivery_svg__a" style="mask-type:alpha"
                                            maskUnits="userSpaceOnUse" x="0" y="0" width="15" height="12">
                                            <path fill-rule="evenodd" clip-rule="evenodd" d="M15 0H0v11.786h15V0z"
                                                fill="#fff"></path>
                                        </mask>
                                        <g mask="url(#IconProductDelivery_svg__a)">
                                            <path fill-rule="evenodd" clip-rule="evenodd"
                                                d="M.755 9.406c0 .021.022.044.042.044h.734c.174-.879.91-1.54 1.795-1.54.885 0 1.62.661 1.795 1.54H9.88c.174-.879.91-1.54 1.794-1.54s1.621.661 1.795 1.54h.735c.02 0 .041-.023.041-.044V6.289a2.112 2.112 0 00-.142-.672l-1.23-2.73c-.007-.058-.208-.192-.259-.174H9.101c-.021 0-.043.023-.043.045v4.37H.755v2.278zm2.571 1.583c.596-.001 1.078-.51 1.08-1.141-.002-.63-.484-1.14-1.08-1.14-.597 0-1.079.51-1.08 1.14.001.63.483 1.14 1.08 1.14zm8.348 0c.597-.002 1.08-.51 1.08-1.141 0-.63-.483-1.14-1.08-1.141-.596.001-1.079.51-1.08 1.141.001.63.484 1.139 1.08 1.14zM0 6.333V.84C.002.376.356.001.796 0h6.14c.44.002.795.375.796.841v.903h-.755V.841c0-.02-.022-.045-.042-.045H.795c-.019 0-.04.023-.04.045v5.492h7.55V2.758c0-.465.355-.84.796-.84h3.513c.41.017.747.243.939.626l1.23 2.73c.13.302.212.683.217 1.015v3.117c-.002.465-.355.838-.796.84h-.735c-.173.879-.91 1.539-1.795 1.539-.884 0-1.62-.66-1.795-1.54H5.121c-.174.88-.911 1.54-1.795 1.54-.885 0-1.621-.66-1.795-1.54H.797c-.441 0-.795-.374-.797-.84V6.334z"
                                                fill="#959595"></path>
                                        </g>
                                    </svg><span class="blind">배송비</span>무료</span></span></strong></div>
                    <div class="basicList_depth__SbZWF"><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">식품</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">통조림/캔</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">햄</span></div>
                    <div class="basicList_desc__3kwkT">
                        <div class="basicList_ad_event__1TOUD"></div>
                    </div>
                    <div class="basicList_etc_box__5lkgg"><span class="basicList_etc__LSkN_">등록일
                            <!-- -->2022.11.</span><span class="basicList_etc__LSkN_"><a href="#" role="button"
                                class="basicList_btn_zzim__YCRGy N=a:lst*A.mylist,i:85050028140,r:1"
                                data-nclick="N=a:lst*A.mylist,i:85050028140,r:1" data-i="85050028140"
                                data-testid="ZZIM_BUTTON"><svg width="16" height="14" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="basicList_svg_zzim__rw2qP">
                                    <path
                                        d="M6.812 2.02a3.345 3.345 0 00-4.81 0C.665 3.381.665 5.601 2 6.966L7.988 13l6.179-6.224c1.167-1.355 1.105-3.455-.168-4.756A3.337 3.337 0 0011.594 1c-.91 0-1.764.361-2.407 1.02L6.543 4.692a1.7 1.7 0 000 2.424c.676.67 1.778.67 2.456 0l2.577-2.594"
                                        stroke="currentcolor"></path>
                                </svg><span class="basicList_text__gCaiD">찜하기<em
                                        class="basicList_num__sfz3h">121</em></span></a></span><span
                            class="basicList_etc__LSkN_"><a href="#" class="report_link_report__pkIEk"
                                data-nclick="N=a:lst*A.report,i:85050028140,r:1"
                                data-testid="SEARCH_PRODUCT_REPORT"><svg width="14" height="14" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="report_svg_report__xPbmh">
                                    <path clip-rule="evenodd" d="M6.999 1A4.999 4.999 0 002 6v4h10V6a5 5 0 00-5.001-5z"
                                        stroke="#999" stroke-linejoin="round"></path>
                                    <path d="M6.5 3.5a2 2 0 00-2 2" stroke="#999"></path>
                                    <path clip-rule="evenodd" d="M1 13h12v-3H1v3z" stroke="#999"></path>
                                </svg>신고하기</a></span></div>
                </div>
                <div class="basicList_mall_area__faH62">
                    <div class="basicList_mall_title__FDXX5"><a target="_blank" class="basicList_mall__BC5Xu"
                            rel="noopener" data-nclick="N=a:lst*A.mall,i:85050028140,r:1"
                            href="https://adcr.naver.com/adcr?x=pWXquo+6HIn6Vhh8oER1QP///w==kA6Fn1FQzMP2q8RN3peUFDrf/AFh7R/LnY2itBKt3P8x+wJqHD7kAUDpP7gjTCPMq6cSxPo0lvZQQstDt9SdR8LVFNVoJ5GMdANVhfH1avLulmWsVXTmBdJE6KZ6S8ujrwX1kNqhMhb66guU7GrOaXomdtnEK2iMCs7ON9BM+lbQbsccMz3bKRzlg1bowmf5bBexDIrreIG+QlmxMgr4Za1ZzAOxUloGnIpnW3JfsDBUol1502mJl6t4gugNXJs8Pq5IQZb7d1m3+xPUMIbtKAsQzm3fSaYY4VjPl4np4QepsicvcYmUMlfm4a12+HgZ/eYjHVGZgRRZ0B+uHO3thAgSpoGqj2KKHov9jYExOfkHXg1TzT6Hh8+EAX5gWwikR2jlFUYVferMBwMElCvUDo/CK/Kf7blrh1HHnoMTpC8xdm+q5F5/v/CXrtj2HoV5e+311hK1evJHF1h32OPIfXvFuVN5SATvn1roC4uInZ0vlI1e85ymf8vAGpa/Efm7DBzQWZEV7Xnab3kxdRlzZG5qa4WYfjH+h6BIZSNO5vGanyAid8DxpmJtJ62pOoErm3O+Kh0IpXOTVoZSYp+clxqH78G6Ognsg04ogGmMv+sBMnHI2Vj6sabI03/vr4dxRyBH4/lmqj7sSPbDloO0x5qbELGYmo+W1D7uuIWrPOnpYX0GX9gtMzyTvQbJtL+QvjbpdIs5QH0yLpEJOz261a1xHT3BePpK+i/u7bQMFIWWAs7Eam3PK6xngyUSOK7EnjTmqpd3mOZ6TvLKCUCUy6gbWdlrBRwwKQ1c0hPyaCZ60txd662SznsojDkEH++bUus/r6c+3t0TJAaE/j3Tft8Psv4JFbceJCEzcoSFiMTBS0yktkiX2hUfFcyMC2O78M9xdzehJLchi9bHPJYvyGhwsJHYIggaThTbbcz+rx5g=">씨제이제일제당</a><button
                            type="button" class="common_btn_detail__s22a_">정보</button><a href="#"
                            class="basicList_link_more__gwqYh">상품만 보기</a></div>
                    <div class="basicList_mall_grade__1hPzs"><span class="basicList_grade__unbQp"><img
                                src="https://ssl.pstatic.net/shoppingsearch/static/pc/pc-230110-131914/img/search/premium_v1.png"
                                alt="씨제이제일제당">프리미엄</span><span class="basicList_grade__unbQp">굿서비스</span></div>
                    <div class="basicList_brand_store__qUCFA">브랜드스토어</div>
                    <ul class="basicList_mall_option__dJLWd">
                        <li><span class="basicList_ico_public__oIoRZ"><svg width="23" height="13" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="svg_public">
                                    <path
                                        d="M1 .5h21c.312 0 .5.226.5.429V12.07c0 .203-.188.429-.5.429H1c-.312 0-.5-.226-.5-.429V.93C.5.726.688.5 1 .5z"
                                        fill="#fff" stroke="#60A2ED"></path>
                                    <path
                                        d="M10.53 9.05c0-1.01-1.07-1.64-3.02-1.64-1.96 0-3.05.63-3.05 1.64 0 1 1.09 1.63 3.05 1.63 1.95 0 3.02-.63 3.02-1.63zm.96-2.29v-.72H7.7V4.22h-.88v1.82H3.6v.72h7.89zM9.63 9.05c0 .6-.83.92-2.12.92-1.31 0-2.14-.32-2.14-.92 0-.59.83-.92 2.14-.92 1.29 0 2.12.33 2.12.92zm.92-6.63h-6v.72h5.11c0 .75-.05 1.58-.23 2.27.29.04.58.08.86.11.14-.59.23-1.45.25-2.23 0-.29.01-.54.01-.87zm8.572 4.73V1.97h-.89v5.18h.89zm-1.88-1.17c-1-.35-2.17-1.4-2.17-2.85v-.81h-.91v.85c0 1.43-1.04 2.55-2.27 3.08l.54.68c1-.49 1.93-1.41 2.19-2.31.37.87 1.32 1.69 2.1 2.04l.52-.68zm1.88 4.73V7.62h-5.86v.72h4.97v2.37h.89z"
                                        fill="#4C97EA"></path>
                                </svg><span class="blind">공식몰</span></span><span class="n_npay_info__xZATR"><span
                                    class="n_npay_icon__DxpI2" data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                        class="blind">네이버플러스멤버십</span><svg xmlns="http://www.w3.org/2000/svg" width="42"
                                        height="13" viewBox="0 0 42 13">
                                        <g fill="none" fill-rule="evenodd">
                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                            </path>
                                            <path fill="#FFF" fill-rule="nonzero"
                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                            </path>
                                            <path fill="#03C75A"
                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                            </path>
                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                            <path fill="#03C75A" fill-rule="nonzero"
                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                            </path>
                                            <path fill="#FFF" fill-rule="nonzero"
                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                            </path>
                                        </g>
                                    </svg></span></span><span class="n_npay_info__TqvjM"><span>포인트 1,056원</span></span>
                        </li>
                        <li><em class="basicList_option__iDFgy">할인</em><button type="button"
                                class="common_btn_detail__s22a_" data-nclick="N=a:lst*A.detail">구매정보</button></li>
                    </ul>
                </div>
            </div>
        </li>
    </div>
    <div>
        <li class="basicList_item__0T9JD ad">
            <div class="basicList_inner__xCM3J">
                <div class="basicList_img_area__AdRY_">
                    <div class="thumbnail_thumb_wrap__RbcYO _wrapper"><a target="_blank" class="thumbnail_thumb__Bxb6Z"
                            rel="noopener" data-nclick="N=a:lst*A.image,r:2,i:83964896618"
                            data-testid="SEARCH_PRODUCT_AD"
                            href="https://adcr.naver.com/adcr?x=JVWKBhqec+KwJwOfzjN5lv///w==k/vfeqzknwLCnAk2XB1DIznYIu54g2vxOMI9BTe7b6CrQgmlh1QVlVpuU5t3TgjqRbMuyAwiUbbUXZ32HEZFFxZVtqdFXeBA5h+1qZ1sMsZK9FPWdwfQt+fnab2AUXJL4NKI98yg/lruzelv7/taP/44Y/qxTXvlomyjqeHE4EGBjSptA30Vd5sm0GBADTvZJ/9qFy9WPziTrgBr4lqy8be3Jy6UgOnO/e7tPf7vwxlI0Vd95VCdKKxFMe/43R32EZkAwIqnHjOEjvJ9WPMnEAC6k/SXs/8qaNw6zBsxSYPy1dKA+mJkxcT7zxc8Of6F1mXoJlwpwUfib/Y0vwzZJMlCZH9dbvAQ5syJZg4Pif1ew5GBYB062iLFU7SsU3Ahac/DalvJdj5fwgrvzspiV0K27r2asnACTrV1T+TMb+Lj0a8O5cOEGCiU9vwMWwQk4BqnuGNDg3kAvCZgnX5/We7nJ082hYkSKta07WW9Nj9XulkT60tKUTbccOqYcPWpUYzz+NE3VQ1f9dp7gW/8KloavSpwfS2K/ApFO6kaNqbK7P79Q8l2jh7q/r85Xx0vJYORoqjDmqC3Vk9JXDTplA9XOI3+nkSdYec/N3m2jmQPLR6FVqJ5fejCVQv+kW9atnbR2v4d3YiETSMB/KVK16KyvS3KWBTEq3+GeOThwkBlGPf8f4i/rQ08wYHOnxQfwlKRB2PkW+WUkLyCZkB4GiewMJny5IE7dKv7qCNzXAYhB1NqeMSCe0fORvble1KJy4X6KrJBb65xxLer22Ke5HxeKWvigyk70+VpcQFTozFsRyvSbM3OHIHskzv5GkG63VXvVccqvQWJQm0LFHGW33FzL5k/R9ldBzOqzBDQmozUGzpSL7Pzn11+pUXXGYMZdAEt/rBxvBcdKUnIUQc9aolzrBlAUz2+FsEMv4h313Ac="><img
                                width="140" height="140" alt="스팸클래식 200Gx10개"
                                src="https://shopping-phinf.pstatic.net/main_8396489/83964896618.1.jpg?type=f140"></a>
                        <div class="thumbnail_btn_box____IiP">
                            <div class="thumbnail_btn__3Gjg1"><button type="button" class="thumbnail_save__yu3R_"
                                    data-nclick="N=a:lst*A.put"><span
                                        class="thumbnail_layer_info__r_5dH">담기</span></button>
                                <div class="thumbnail_layer_info__r_5dH">
                                    <div class="thumbnail_link_box__fhsB8"><a href="#" class="thumbnail_link__i3ShY"
                                            data-nclick="N=a:lst*A.putblog">내 블로그에 담기</a><a href="#"
                                            class="thumbnail_link__i3ShY" data-nclick="N=a:lst*A.putcafe">카페에 담기</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="basicList_info_area__TWvzp">
                    <div class="basicList_title__VfX3c"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*A.title,i:83964896618,r:2" data-testid="SEARCH_PRODUCT_AD"
                            title="스팸클래식 200Gx10개"
                            href="https://adcr.naver.com/adcr?x=JVWKBhqec+KwJwOfzjN5lv///w==k/vfeqzknwLCnAk2XB1DIznYIu54g2vxOMI9BTe7b6CrQgmlh1QVlVpuU5t3TgjqRbMuyAwiUbbUXZ32HEZFFxZVtqdFXeBA5h+1qZ1sMsZK9FPWdwfQt+fnab2AUXJL4NKI98yg/lruzelv7/taP/44Y/qxTXvlomyjqeHE4EGBjSptA30Vd5sm0GBADTvZJ/9qFy9WPziTrgBr4lqy8be3Jy6UgOnO/e7tPf7vwxlI0Vd95VCdKKxFMe/43R32EZkAwIqnHjOEjvJ9WPMnEAC6k/SXs/8qaNw6zBsxSYPy1dKA+mJkxcT7zxc8Of6F1mXoJlwpwUfib/Y0vwzZJMlCZH9dbvAQ5syJZg4Pif1ew5GBYB062iLFU7SsU3Ahac/DalvJdj5fwgrvzspiV0K27r2asnACTrV1T+TMb+Lj0a8O5cOEGCiU9vwMWwQk4BqnuGNDg3kAvCZgnX5/We7nJ082hYkSKta07WW9Nj9XulkT60tKUTbccOqYcPWpUYzz+NE3VQ1f9dp7gW/8KloavSpwfS2K/ApFO6kaNqbK7P79Q8l2jh7q/r85Xx0vJYORoqjDmqC3Vk9JXDTplA9XOI3+nkSdYec/N3m2jmQPLR6FVqJ5fejCVQv+kW9atnbR2v4d3YiETSMB/KVK16KyvS3KWBTEq3+GeOThwkBlGPf8f4i/rQ08wYHOnxQfwlKRB2PkW+WUkLyCZkB4GiewMJny5IE7dKv7qCNzXAYhB1NqeMSCe0fORvble1KJy4X6KrJBb65xxLer22Ke5HxeKWvigyk70+VpcQFTozFsRyvSbM3OHIHskzv5GkG63VXvVccqvQWJQm0LFHGW33FzL5k/R9ldBzOqzBDQmozUGzpSL7Pzn11+pUXXGYMZdAEt/rBxvBcdKUnIUQc9aolzrBlAUz2+FsEMv4h313Ac=">스팸클래식
                            200Gx10개</a></div>
                    <div class="basicList_price_area__K7DDT"><button type="button"
                            class="ad_ad_stk__pBe5A">광고</button><strong class="basicList_price__euNoD"><span><span
                                    class="price_num__S2p_v" data-testid="SEARCH_PRODUCT_PRICE">39,800원</span><span
                                    class="price_delivery__yw_We"><svg width="15" height="12" fill="none"
                                        xmlns="http://www.w3.org/2000/svg" class="price_svg_delivery__kOiSU">
                                        <mask id="IconProductDelivery_svg__a" style="mask-type:alpha"
                                            maskUnits="userSpaceOnUse" x="0" y="0" width="15" height="12">
                                            <path fill-rule="evenodd" clip-rule="evenodd" d="M15 0H0v11.786h15V0z"
                                                fill="#fff"></path>
                                        </mask>
                                        <g mask="url(#IconProductDelivery_svg__a)">
                                            <path fill-rule="evenodd" clip-rule="evenodd"
                                                d="M.755 9.406c0 .021.022.044.042.044h.734c.174-.879.91-1.54 1.795-1.54.885 0 1.62.661 1.795 1.54H9.88c.174-.879.91-1.54 1.794-1.54s1.621.661 1.795 1.54h.735c.02 0 .041-.023.041-.044V6.289a2.112 2.112 0 00-.142-.672l-1.23-2.73c-.007-.058-.208-.192-.259-.174H9.101c-.021 0-.043.023-.043.045v4.37H.755v2.278zm2.571 1.583c.596-.001 1.078-.51 1.08-1.141-.002-.63-.484-1.14-1.08-1.14-.597 0-1.079.51-1.08 1.14.001.63.483 1.14 1.08 1.14zm8.348 0c.597-.002 1.08-.51 1.08-1.141 0-.63-.483-1.14-1.08-1.141-.596.001-1.079.51-1.08 1.141.001.63.484 1.139 1.08 1.14zM0 6.333V.84C.002.376.356.001.796 0h6.14c.44.002.795.375.796.841v.903h-.755V.841c0-.02-.022-.045-.042-.045H.795c-.019 0-.04.023-.04.045v5.492h7.55V2.758c0-.465.355-.84.796-.84h3.513c.41.017.747.243.939.626l1.23 2.73c.13.302.212.683.217 1.015v3.117c-.002.465-.355.838-.796.84h-.735c-.173.879-.91 1.539-1.795 1.539-.884 0-1.62-.66-1.795-1.54H5.121c-.174.88-.911 1.54-1.795 1.54-.885 0-1.621-.66-1.795-1.54H.797c-.441 0-.795-.374-.797-.84V6.334z"
                                                fill="#959595"></path>
                                        </g>
                                    </svg><span class="blind">배송비</span>무료</span></span></strong></div>
                    <div class="basicList_depth__SbZWF"><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">식품</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">통조림/캔</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">햄</span></div>
                    <div class="basicList_desc__3kwkT">
                        <div class="basicList_ad_event__1TOUD"></div>
                    </div>
                    <div class="basicList_etc_box__5lkgg"><span class="basicList_etc__LSkN_">등록일
                            <!-- -->2022.03.</span><span class="basicList_etc__LSkN_"><a href="#" role="button"
                                class="basicList_btn_zzim__YCRGy N=a:lst*A.mylist,i:83964896618,r:2"
                                data-nclick="N=a:lst*A.mylist,i:83964896618,r:2" data-i="83964896618"
                                data-testid="ZZIM_BUTTON"><svg width="16" height="14" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="basicList_svg_zzim__rw2qP">
                                    <path
                                        d="M6.812 2.02a3.345 3.345 0 00-4.81 0C.665 3.381.665 5.601 2 6.966L7.988 13l6.179-6.224c1.167-1.355 1.105-3.455-.168-4.756A3.337 3.337 0 0011.594 1c-.91 0-1.764.361-2.407 1.02L6.543 4.692a1.7 1.7 0 000 2.424c.676.67 1.778.67 2.456 0l2.577-2.594"
                                        stroke="currentcolor"></path>
                                </svg><span class="basicList_text__gCaiD">찜하기<em
                                        class="basicList_num__sfz3h">1228</em></span></a></span><span
                            class="basicList_etc__LSkN_"><a href="#" class="report_link_report__pkIEk"
                                data-nclick="N=a:lst*A.report,i:83964896618,r:2"
                                data-testid="SEARCH_PRODUCT_REPORT"><svg width="14" height="14" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="report_svg_report__xPbmh">
                                    <path clip-rule="evenodd" d="M6.999 1A4.999 4.999 0 002 6v4h10V6a5 5 0 00-5.001-5z"
                                        stroke="#999" stroke-linejoin="round"></path>
                                    <path d="M6.5 3.5a2 2 0 00-2 2" stroke="#999"></path>
                                    <path clip-rule="evenodd" d="M1 13h12v-3H1v3z" stroke="#999"></path>
                                </svg>신고하기</a></span></div>
                </div>
                <div class="basicList_mall_area__faH62">
                    <div class="basicList_mall_title__FDXX5"><a target="_blank" class="basicList_mall__BC5Xu"
                            rel="noopener" data-nclick="N=a:lst*A.mall,i:83964896618,r:2"
                            href="https://adcr.naver.com/adcr?x=JVWKBhqec+KwJwOfzjN5lv///w==k/vfeqzknwLCnAk2XB1DIznYIu54g2vxOMI9BTe7b6CrQgmlh1QVlVpuU5t3TgjqRbMuyAwiUbbUXZ32HEZFFxZVtqdFXeBA5h+1qZ1sMsZK9FPWdwfQt+fnab2AUXJL4NKI98yg/lruzelv7/taP/44Y/qxTXvlomyjqeHE4EGBjSptA30Vd5sm0GBADTvZJ/9qFy9WPziTrgBr4lqy8be3Jy6UgOnO/e7tPf7vwxlI0Vd95VCdKKxFMe/43R32EZkAwIqnHjOEjvJ9WPMnEAC6k/SXs/8qaNw6zBsxSYPy1dKA+mJkxcT7zxc8Of6F1mXoJlwpwUfib/Y0vwzZJMlCZH9dbvAQ5syJZg4Pif1ew5GBYB062iLFU7SsU3Ahac/DalvJdj5fwgrvzspiV0K27r2asnACTrV1T+TMb+Lj0a8O5cOEGCiU9vwMWwQk4BqnuGNDg3kAvCZgnX5/We7nJ082hYkSKta07WW9Nj9XulkT60tKUTbccOqYcPWpUYzz+NE3VQ1f9dp7gW/8KloavSpwfS2K/ApFO6kaNqbK7P79Q8l2jh7q/r85Xx0vJYORoqjDmqC3Vk9JXDTplA9XOI3+nkSdYec/N3m2jmQPLR6FVqJ5fejCVQv+kW9atnbR2v4d3YiETSMB/KVK16KyvS3KWBTEq3+GeOThwkBlGPf8f4i/rQ08wYHOnxQfwlKRB2PkW+WUkLyCZkB4GiewMJny5IE7dKv7qCNzXAYhB1NqeMSCe0fORvble1KJy4X6KrJBb65xxLer22Ke5HxeKWvigyk70+VpcQFTozFsRyvSbM3OHIHskzv5GkG63VXvVccqvQWJQm0LFHGW33FzL5k/R9ldBzOqzBDQmozUGzpSL7Pzn11+pUXXGYMZdAEt/rBxvBcdKUnIUQc9aolzrBlAUz2+FsEMv4h313Ac=">씨제이제일제당</a><button
                            type="button" class="common_btn_detail__s22a_">정보</button><a href="#"
                            class="basicList_link_more__gwqYh">상품만 보기</a></div>
                    <div class="basicList_mall_grade__1hPzs"><span class="basicList_grade__unbQp"><img
                                src="https://ssl.pstatic.net/shoppingsearch/static/pc/pc-230110-131914/img/search/premium_v1.png"
                                alt="씨제이제일제당">프리미엄</span><span class="basicList_grade__unbQp">굿서비스</span></div>
                    <div class="basicList_brand_store__qUCFA">브랜드스토어</div>
                    <ul class="basicList_mall_option__dJLWd">
                        <li><span class="basicList_ico_public__oIoRZ"><svg width="23" height="13" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="svg_public">
                                    <path
                                        d="M1 .5h21c.312 0 .5.226.5.429V12.07c0 .203-.188.429-.5.429H1c-.312 0-.5-.226-.5-.429V.93C.5.726.688.5 1 .5z"
                                        fill="#fff" stroke="#60A2ED"></path>
                                    <path
                                        d="M10.53 9.05c0-1.01-1.07-1.64-3.02-1.64-1.96 0-3.05.63-3.05 1.64 0 1 1.09 1.63 3.05 1.63 1.95 0 3.02-.63 3.02-1.63zm.96-2.29v-.72H7.7V4.22h-.88v1.82H3.6v.72h7.89zM9.63 9.05c0 .6-.83.92-2.12.92-1.31 0-2.14-.32-2.14-.92 0-.59.83-.92 2.14-.92 1.29 0 2.12.33 2.12.92zm.92-6.63h-6v.72h5.11c0 .75-.05 1.58-.23 2.27.29.04.58.08.86.11.14-.59.23-1.45.25-2.23 0-.29.01-.54.01-.87zm8.572 4.73V1.97h-.89v5.18h.89zm-1.88-1.17c-1-.35-2.17-1.4-2.17-2.85v-.81h-.91v.85c0 1.43-1.04 2.55-2.27 3.08l.54.68c1-.49 1.93-1.41 2.19-2.31.37.87 1.32 1.69 2.1 2.04l.52-.68zm1.88 4.73V7.62h-5.86v.72h4.97v2.37h.89z"
                                        fill="#4C97EA"></path>
                                </svg><span class="blind">공식몰</span></span><span class="n_npay_info__xZATR"><span
                                    class="n_npay_icon__DxpI2" data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                        class="blind">네이버플러스멤버십</span><svg xmlns="http://www.w3.org/2000/svg" width="42"
                                        height="13" viewBox="0 0 42 13">
                                        <g fill="none" fill-rule="evenodd">
                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                            </path>
                                            <path fill="#FFF" fill-rule="nonzero"
                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                            </path>
                                            <path fill="#03C75A"
                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                            </path>
                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                            <path fill="#03C75A" fill-rule="nonzero"
                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                            </path>
                                            <path fill="#FFF" fill-rule="nonzero"
                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                            </path>
                                        </g>
                                    </svg></span></span><span class="n_npay_info__TqvjM"><span>포인트 796원</span></span>
                        </li>
                        <li><em class="basicList_option__iDFgy">할인</em><button type="button"
                                class="common_btn_detail__s22a_" data-nclick="N=a:lst*A.detail">구매정보</button></li>
                    </ul>
                </div>
            </div>
        </li>
    </div>
    <div>
        <li class="basicList_item__0T9JD ad">
            <div class="basicList_inner__xCM3J">
                <div class="basicList_img_area__AdRY_">
                    <div class="thumbnail_thumb_wrap__RbcYO _wrapper"><a target="_blank" class="thumbnail_thumb__Bxb6Z"
                            rel="noopener" data-nclick="N=a:lst*A.image,r:3,i:85141263465"
                            data-testid="SEARCH_PRODUCT_AD"
                            href="https://adcr.naver.com/adcr?x=55XlyVyIt2PJ34A7tAbXQf///w==kR7FEZWz8pwLYrbptbx3SB4XHWzpKsXlL32miWdhahBVfkdQgLuZzM6s8KGJlUYzob5RINDX4F8df/w3mNezarkKBs7PpDq/OAPkvmhEOGM/J1mV9bQo7eVoceEvD75/h6NJdrNeRN8AoknqX4zEv4KfgwENep5dJHYKuJglJytI4U1S2QzMtgIzqsnNLpzW17M56ntE7Mlk/6d/Fob5u9ZSzA7d6Lf79HzyGPwsYinPrsSLE7OJWRRmNgiGzqRM7kn8hTD+Ym+TpjhdRrstneo42ePtXyAQSWktcd54GVY8RERTjmVlYpLb5XZSskvF6bMyPrenE5cPG3sYQAP0Hzx/XpgE/ziVVY1SRAF8OFE4oAYrULmucu383t9UCT0kWsLEoROP5dg0RgUacdaldaq9ychnZyoyXkX1aAMfjZmoSPjHZ+EHkI/d6Ox8vPXU3ZhZ60ltzophimCj4XaEy+biROCiXeWaMbFaHmNsTALlLFPWPG8IEh6w0BaGOvBzjP3rKKHHemFTClsE6qQAjgRjYgOkBhxJeFCz2ks0yWAwgH0oJBWmey6oLj3qI4yZkt4wQpe3khW7XTqCDz+hIwoA49HgPWTwMEjbWS/oFQXW71QMN6KJLvieR+Hqq7BBdgq4/80ZdDmmIVo0IRgtXUZzhKTJ2RV9Lt2XWBYggFBzkG+/6McTqRrnLku9fSKyaKjTiBzDuM9jnQ4csancz/3iFZyJXygIYORTWB/A2iQHZqaB7uYw4z1XI17/OWC1if4RIVttNFRapaAnfBUq+KVfHPpZoXnRKBiDrIy4HYhaxBPgrf8hZVmuWz/zY77E+xYZucXM+ro2AjT69pWaY42txMdg3SCR7B6t1pKW8pNpaLfHr54Zi607plQdS55CPUwbYy/Gs6kWuFns/mvbQI+MYLVuYkrxjACXnybfliNU="><img
                                width="140" height="140" alt="스팸 클래식 340Gx8개"
                                src="https://shopping-phinf.pstatic.net/main_8514126/85141263465.1.jpg?type=f140"></a>
                        <div class="thumbnail_btn_box____IiP">
                            <div class="thumbnail_btn__3Gjg1"><button type="button" class="thumbnail_save__yu3R_"
                                    data-nclick="N=a:lst*A.put"><span
                                        class="thumbnail_layer_info__r_5dH">담기</span></button>
                                <div class="thumbnail_layer_info__r_5dH">
                                    <div class="thumbnail_link_box__fhsB8"><a href="#" class="thumbnail_link__i3ShY"
                                            data-nclick="N=a:lst*A.putblog">내 블로그에 담기</a><a href="#"
                                            class="thumbnail_link__i3ShY" data-nclick="N=a:lst*A.putcafe">카페에 담기</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="basicList_info_area__TWvzp">
                    <div class="basicList_title__VfX3c"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*A.title,i:85141263465,r:3" data-testid="SEARCH_PRODUCT_AD"
                            title="스팸 클래식 340Gx8개"
                            href="https://adcr.naver.com/adcr?x=55XlyVyIt2PJ34A7tAbXQf///w==kR7FEZWz8pwLYrbptbx3SB4XHWzpKsXlL32miWdhahBVfkdQgLuZzM6s8KGJlUYzob5RINDX4F8df/w3mNezarkKBs7PpDq/OAPkvmhEOGM/J1mV9bQo7eVoceEvD75/h6NJdrNeRN8AoknqX4zEv4KfgwENep5dJHYKuJglJytI4U1S2QzMtgIzqsnNLpzW17M56ntE7Mlk/6d/Fob5u9ZSzA7d6Lf79HzyGPwsYinPrsSLE7OJWRRmNgiGzqRM7kn8hTD+Ym+TpjhdRrstneo42ePtXyAQSWktcd54GVY8RERTjmVlYpLb5XZSskvF6bMyPrenE5cPG3sYQAP0Hzx/XpgE/ziVVY1SRAF8OFE4oAYrULmucu383t9UCT0kWsLEoROP5dg0RgUacdaldaq9ychnZyoyXkX1aAMfjZmoSPjHZ+EHkI/d6Ox8vPXU3ZhZ60ltzophimCj4XaEy+biROCiXeWaMbFaHmNsTALlLFPWPG8IEh6w0BaGOvBzjP3rKKHHemFTClsE6qQAjgRjYgOkBhxJeFCz2ks0yWAwgH0oJBWmey6oLj3qI4yZkt4wQpe3khW7XTqCDz+hIwoA49HgPWTwMEjbWS/oFQXW71QMN6KJLvieR+Hqq7BBdgq4/80ZdDmmIVo0IRgtXUZzhKTJ2RV9Lt2XWBYggFBzkG+/6McTqRrnLku9fSKyaKjTiBzDuM9jnQ4csancz/3iFZyJXygIYORTWB/A2iQHZqaB7uYw4z1XI17/OWC1if4RIVttNFRapaAnfBUq+KVfHPpZoXnRKBiDrIy4HYhaxBPgrf8hZVmuWz/zY77E+xYZucXM+ro2AjT69pWaY42txMdg3SCR7B6t1pKW8pNpaLfHr54Zi607plQdS55CPUwbYy/Gs6kWuFns/mvbQI+MYLVuYkrxjACXnybfliNU=">스팸
                            클래식 340Gx8개</a></div>
                    <div class="basicList_price_area__K7DDT"><button type="button"
                            class="ad_ad_stk__pBe5A">광고</button><strong class="basicList_price__euNoD"><span><span
                                    class="price_num__S2p_v" data-testid="SEARCH_PRODUCT_PRICE">31,980원</span><span
                                    class="price_delivery__yw_We"><svg width="15" height="12" fill="none"
                                        xmlns="http://www.w3.org/2000/svg" class="price_svg_delivery__kOiSU">
                                        <mask id="IconProductDelivery_svg__a" style="mask-type:alpha"
                                            maskUnits="userSpaceOnUse" x="0" y="0" width="15" height="12">
                                            <path fill-rule="evenodd" clip-rule="evenodd" d="M15 0H0v11.786h15V0z"
                                                fill="#fff"></path>
                                        </mask>
                                        <g mask="url(#IconProductDelivery_svg__a)">
                                            <path fill-rule="evenodd" clip-rule="evenodd"
                                                d="M.755 9.406c0 .021.022.044.042.044h.734c.174-.879.91-1.54 1.795-1.54.885 0 1.62.661 1.795 1.54H9.88c.174-.879.91-1.54 1.794-1.54s1.621.661 1.795 1.54h.735c.02 0 .041-.023.041-.044V6.289a2.112 2.112 0 00-.142-.672l-1.23-2.73c-.007-.058-.208-.192-.259-.174H9.101c-.021 0-.043.023-.043.045v4.37H.755v2.278zm2.571 1.583c.596-.001 1.078-.51 1.08-1.141-.002-.63-.484-1.14-1.08-1.14-.597 0-1.079.51-1.08 1.14.001.63.483 1.14 1.08 1.14zm8.348 0c.597-.002 1.08-.51 1.08-1.141 0-.63-.483-1.14-1.08-1.141-.596.001-1.079.51-1.08 1.141.001.63.484 1.139 1.08 1.14zM0 6.333V.84C.002.376.356.001.796 0h6.14c.44.002.795.375.796.841v.903h-.755V.841c0-.02-.022-.045-.042-.045H.795c-.019 0-.04.023-.04.045v5.492h7.55V2.758c0-.465.355-.84.796-.84h3.513c.41.017.747.243.939.626l1.23 2.73c.13.302.212.683.217 1.015v3.117c-.002.465-.355.838-.796.84h-.735c-.173.879-.91 1.539-1.795 1.539-.884 0-1.62-.66-1.795-1.54H5.121c-.174.88-.911 1.54-1.795 1.54-.885 0-1.621-.66-1.795-1.54H.797c-.441 0-.795-.374-.797-.84V6.334z"
                                                fill="#959595"></path>
                                        </g>
                                    </svg><span class="blind">배송비</span>무료</span></span></strong></div>
                    <div class="basicList_depth__SbZWF"><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">식품</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">통조림/캔</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">햄</span></div>
                    <div class="basicList_desc__3kwkT">
                        <div class="basicList_ad_event__1TOUD"></div>
                    </div>
                    <div class="basicList_etc_box__5lkgg"><span class="basicList_etc__LSkN_">등록일
                            <!-- -->2022.11.</span><span class="basicList_etc__LSkN_"><a href="#" role="button"
                                class="basicList_btn_zzim__YCRGy N=a:lst*A.mylist,i:85141263465,r:3"
                                data-nclick="N=a:lst*A.mylist,i:85141263465,r:3" data-i="85141263465"
                                data-testid="ZZIM_BUTTON"><svg width="16" height="14" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="basicList_svg_zzim__rw2qP">
                                    <path
                                        d="M6.812 2.02a3.345 3.345 0 00-4.81 0C.665 3.381.665 5.601 2 6.966L7.988 13l6.179-6.224c1.167-1.355 1.105-3.455-.168-4.756A3.337 3.337 0 0011.594 1c-.91 0-1.764.361-2.407 1.02L6.543 4.692a1.7 1.7 0 000 2.424c.676.67 1.778.67 2.456 0l2.577-2.594"
                                        stroke="currentcolor"></path>
                                </svg><span class="basicList_text__gCaiD">찜하기<em
                                        class="basicList_num__sfz3h">188</em></span></a></span><span
                            class="basicList_etc__LSkN_"><a href="#" class="report_link_report__pkIEk"
                                data-nclick="N=a:lst*A.report,i:85141263465,r:3"
                                data-testid="SEARCH_PRODUCT_REPORT"><svg width="14" height="14" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="report_svg_report__xPbmh">
                                    <path clip-rule="evenodd" d="M6.999 1A4.999 4.999 0 002 6v4h10V6a5 5 0 00-5.001-5z"
                                        stroke="#999" stroke-linejoin="round"></path>
                                    <path d="M6.5 3.5a2 2 0 00-2 2" stroke="#999"></path>
                                    <path clip-rule="evenodd" d="M1 13h12v-3H1v3z" stroke="#999"></path>
                                </svg>신고하기</a></span></div>
                </div>
                <div class="basicList_mall_area__faH62">
                    <div class="basicList_mall_title__FDXX5"><a target="_blank" class="basicList_mall__BC5Xu"
                            rel="noopener" data-nclick="N=a:lst*A.mall,i:85141263465,r:3"
                            href="https://adcr.naver.com/adcr?x=55XlyVyIt2PJ34A7tAbXQf///w==kR7FEZWz8pwLYrbptbx3SB4XHWzpKsXlL32miWdhahBVfkdQgLuZzM6s8KGJlUYzob5RINDX4F8df/w3mNezarkKBs7PpDq/OAPkvmhEOGM/J1mV9bQo7eVoceEvD75/h6NJdrNeRN8AoknqX4zEv4KfgwENep5dJHYKuJglJytI4U1S2QzMtgIzqsnNLpzW17M56ntE7Mlk/6d/Fob5u9ZSzA7d6Lf79HzyGPwsYinPrsSLE7OJWRRmNgiGzqRM7kn8hTD+Ym+TpjhdRrstneo42ePtXyAQSWktcd54GVY8RERTjmVlYpLb5XZSskvF6bMyPrenE5cPG3sYQAP0Hzx/XpgE/ziVVY1SRAF8OFE4oAYrULmucu383t9UCT0kWsLEoROP5dg0RgUacdaldaq9ychnZyoyXkX1aAMfjZmoSPjHZ+EHkI/d6Ox8vPXU3ZhZ60ltzophimCj4XaEy+biROCiXeWaMbFaHmNsTALlLFPWPG8IEh6w0BaGOvBzjP3rKKHHemFTClsE6qQAjgRjYgOkBhxJeFCz2ks0yWAwgH0oJBWmey6oLj3qI4yZkt4wQpe3khW7XTqCDz+hIwoA49HgPWTwMEjbWS/oFQXW71QMN6KJLvieR+Hqq7BBdgq4/80ZdDmmIVo0IRgtXUZzhKTJ2RV9Lt2XWBYggFBzkG+/6McTqRrnLku9fSKyaKjTiBzDuM9jnQ4csancz/3iFZyJXygIYORTWB/A2iQHZqaB7uYw4z1XI17/OWC1if4RIVttNFRapaAnfBUq+KVfHPpZoXnRKBiDrIy4HYhaxBPgrf8hZVmuWz/zY77E+xYZucXM+ro2AjT69pWaY42txMdg3SCR7B6t1pKW8pNpaLfHr54Zi607plQdS55CPUwbYy/Gs6kWuFns/mvbQI+MYLVuYkrxjACXnybfliNU=">씨제이제일제당</a><button
                            type="button" class="common_btn_detail__s22a_">정보</button><a href="#"
                            class="basicList_link_more__gwqYh">상품만 보기</a></div>
                    <div class="basicList_mall_grade__1hPzs"><span class="basicList_grade__unbQp"><img
                                src="https://ssl.pstatic.net/shoppingsearch/static/pc/pc-230110-131914/img/search/premium_v1.png"
                                alt="씨제이제일제당">프리미엄</span><span class="basicList_grade__unbQp">굿서비스</span></div>
                    <div class="basicList_brand_store__qUCFA">브랜드스토어</div>
                    <ul class="basicList_mall_option__dJLWd">
                        <li><span class="basicList_ico_public__oIoRZ"><svg width="23" height="13" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="svg_public">
                                    <path
                                        d="M1 .5h21c.312 0 .5.226.5.429V12.07c0 .203-.188.429-.5.429H1c-.312 0-.5-.226-.5-.429V.93C.5.726.688.5 1 .5z"
                                        fill="#fff" stroke="#60A2ED"></path>
                                    <path
                                        d="M10.53 9.05c0-1.01-1.07-1.64-3.02-1.64-1.96 0-3.05.63-3.05 1.64 0 1 1.09 1.63 3.05 1.63 1.95 0 3.02-.63 3.02-1.63zm.96-2.29v-.72H7.7V4.22h-.88v1.82H3.6v.72h7.89zM9.63 9.05c0 .6-.83.92-2.12.92-1.31 0-2.14-.32-2.14-.92 0-.59.83-.92 2.14-.92 1.29 0 2.12.33 2.12.92zm.92-6.63h-6v.72h5.11c0 .75-.05 1.58-.23 2.27.29.04.58.08.86.11.14-.59.23-1.45.25-2.23 0-.29.01-.54.01-.87zm8.572 4.73V1.97h-.89v5.18h.89zm-1.88-1.17c-1-.35-2.17-1.4-2.17-2.85v-.81h-.91v.85c0 1.43-1.04 2.55-2.27 3.08l.54.68c1-.49 1.93-1.41 2.19-2.31.37.87 1.32 1.69 2.1 2.04l.52-.68zm1.88 4.73V7.62h-5.86v.72h4.97v2.37h.89z"
                                        fill="#4C97EA"></path>
                                </svg><span class="blind">공식몰</span></span><span class="n_npay_info__xZATR"><span
                                    class="n_npay_icon__DxpI2" data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                        class="blind">네이버플러스멤버십</span><svg xmlns="http://www.w3.org/2000/svg" width="42"
                                        height="13" viewBox="0 0 42 13">
                                        <g fill="none" fill-rule="evenodd">
                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                            </path>
                                            <path fill="#FFF" fill-rule="nonzero"
                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                            </path>
                                            <path fill="#03C75A"
                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                            </path>
                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                            <path fill="#03C75A" fill-rule="nonzero"
                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                            </path>
                                            <path fill="#FFF" fill-rule="nonzero"
                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                            </path>
                                        </g>
                                    </svg></span></span><span class="n_npay_info__TqvjM"><span>포인트 638원</span></span>
                        </li>
                        <li><em class="basicList_option__iDFgy">할인</em><button type="button"
                                class="common_btn_detail__s22a_" data-nclick="N=a:lst*A.detail">구매정보</button></li>
                    </ul>
                </div>
            </div>
        </li>
    </div>
    <div>
        <li class="basicList_item__0T9JD">
            <div class="basicList_inner__xCM3J">
                <div class="basicList_img_area__AdRY_">
                    <div class="thumbnail_thumb_wrap__RbcYO _wrapper"><a target="_blank" class="thumbnail_thumb__Bxb6Z"
                            rel="noopener" data-nclick="N=a:lst*C.image,r:1,i:8095458474" data-testid="SEARCH_PRODUCT"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=VsSEXKPY3svzWhnLzbeaVP%2F%2F%2Fw%3D%3DsU1laCgPkdbAROgZdao2X3E01hKsiLLwwg2BmG%2B44QCi9OhgEgWOYg6VLdD%2F7t%2Fdm4RwYAVs%2FBoYH1JBycUa7ZFsZOinTopHxyAyK2u%2FTy%2BjYsfDmngMDc30arSUbghlw8ss4UymE29LknfqYKBhSB5VKLZjQ%2Fw6mGkjrCQya8BrxE5wD2k%2BOpsDqih5IlyNuy%2F6MHZ6u%2F5n6uuzlUc6JNCAYTv5lq0qN%2FmER%2FVdy2QpvuzH7jETdzdbLBEPy40zwub7oD2b6ZN0ODOADdG4X%2FfDsptBh%2F1SQMJZ67RBmboz84irqoupb5cHtoCFQH9lAJV03cukp%2F9sq6JmLvPVclMbjHM9FLNozUIiMWIsXiRwJ3LjRY%2BIkNjZ%2BdiRsKM%2FX0PXurd6BwFrLIufN4yO47dfcgDZbX1uPBgtMBVpOy7Ql0VMPq%2BhwUasLr5wH1EqZSHOsd6oOv8c9AQXdJvlpsKIH%2B1DZs0Gn3b3sxU%2FrvBOYx3ImiOU50eGhoT8AXjXfW3zfdWk0su43MKqtVvUP3UKlLqqrZpAXMAk1bBVmM7BW1Ik0iksMHUM%2B%2FBfeOdoyP4QSzZ0OitoLsmEMWvjVV95ZqgX%2FDU0H0ie07xad3MwdHI8FZtQVGFZJxOyBDKc%2B&amp;nvMid=8095458474&amp;catId=50011943"><img
                                width="140" height="140" alt="CJ제일제당 스팸 클래식 340g"
                                src="https://shopping-phinf.pstatic.net/main_8095458/8095458474.20201006154558.jpg?type=f140"></a>
                        <div class="thumbnail_btn_box____IiP">
                            <div class="thumbnail_btn__3Gjg1"><button type="button" class="thumbnail_save__yu3R_"
                                    data-nclick="N=a:lst*C.put"><span
                                        class="thumbnail_layer_info__r_5dH">담기</span></button>
                                <div class="thumbnail_layer_info__r_5dH">
                                    <div class="thumbnail_link_box__fhsB8"><a href="#" class="thumbnail_link__i3ShY"
                                            data-nclick="N=a:lst*C.putblog">내 블로그에 담기</a><a href="#"
                                            class="thumbnail_link__i3ShY" data-nclick="N=a:lst*C.putcafe">카페에 담기</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="basicList_info_area__TWvzp">
                    <div class="basicList_title__VfX3c"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.title,i:8095458474,r:1" data-testid="SEARCH_PRODUCT"
                            title="CJ제일제당 스팸 클래식 340g"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=VsSEXKPY3svzWhnLzbeaVP%2F%2F%2Fw%3D%3DsU1laCgPkdbAROgZdao2X3E01hKsiLLwwg2BmG%2B44QCi9OhgEgWOYg6VLdD%2F7t%2Fdm4RwYAVs%2FBoYH1JBycUa7ZFsZOinTopHxyAyK2u%2FTy%2BjYsfDmngMDc30arSUbghlw8ss4UymE29LknfqYKBhSB5VKLZjQ%2Fw6mGkjrCQya8BrxE5wD2k%2BOpsDqih5IlyNuy%2F6MHZ6u%2F5n6uuzlUc6JNCAYTv5lq0qN%2FmER%2FVdy2QpvuzH7jETdzdbLBEPy40zwub7oD2b6ZN0ODOADdG4X%2FfDsptBh%2F1SQMJZ67RBmboz84irqoupb5cHtoCFQH9lAJV03cukp%2F9sq6JmLvPVclMbjHM9FLNozUIiMWIsXiRwJ3LjRY%2BIkNjZ%2BdiRsKM%2FX0PXurd6BwFrLIufN4yO47dfcgDZbX1uPBgtMBVpOy7Ql0VMPq%2BhwUasLr5wH1EqZSHOsd6oOv8c9AQXdJvlpsKIH%2B1DZs0Gn3b3sxU%2FrvBOYx3ImiOU50eGhoT8AXjXfW3zfdWk0su43MKqtVvUP3UKlLqqrZpAXMAk1bBVmM7BW1Ik0iksMHUM%2B%2FBfeOdoyP4QSzZ0OitoLsmEMWvjVV95ZqgX%2FDU0H0ie07xad3MwdHI8FZtQVGFZJxOyBDKc%2B&amp;nvMid=8095458474&amp;catId=50011943">CJ제일제당
                            스팸 클래식 340g</a></div>
                    <div class="basicList_price_area__K7DDT"><strong class="basicList_price__euNoD"><span><span
                                    class="price_low__y_ZUj">최저</span><span class="price_num__S2p_v"
                                    data-testid="SEARCH_PRODUCT_PRICE">2,460원</span></span><a target="_blank"
                                class="basicList_compare__d2bWN" rel="noopener"
                                data-nclick="N=a:lst*C.compare,i:8095458474,r:1"
                                href="https://cr.shopping.naver.com/adcr.nhn?x=VsSEXKPY3svzWhnLzbeaVP%2F%2F%2Fw%3D%3DsU1laCgPkdbAROgZdao2X3E01hKsiLLwwg2BmG%2B44QCi9OhgEgWOYg6VLdD%2F7t%2Fdm4RwYAVs%2FBoYH1JBycUa7ZFsZOinTopHxyAyK2u%2FTy%2BjYsfDmngMDc30arSUbghlw8ss4UymE29LknfqYKBhSB5VKLZjQ%2Fw6mGkjrCQya8BrxE5wD2k%2BOpsDqih5IlyNuy%2F6MHZ6u%2F5n6uuzlUc6JNCAYTv5lq0qN%2FmER%2FVdy2QpvuzH7jETdzdbLBEPy40zwub7oD2b6ZN0ODOADdG4X%2FfDsptBh%2F1SQMJZ67RBmboz84irqoupb5cHtoCFQH9lAJV03cukp%2F9sq6JmLvPVclMbjHM9FLNozUIiMWIsXiRwJ3LjRY%2BIkNjZ%2BdiRsKM%2FX0PXurd6BwFrLIufN4yO47dfcgDZbX1uPBgtMBVpOy7Ql0VMPq%2BhwUasLr5wH1EqZSHOsd6oOv8c9AQXdJvlpsKIH%2B1DZs0Gn3b3sxU%2FrvBOYx3ImiOU50eGhoT8AXjXfW3zfdWk0su43MKqtVvUP3UKlLqqrZpAXMAk1bBVmM7BW1Ik0iksMHUM%2B%2FBfeOdoyP4QSzZ0OitoLsmEMWvjVV95ZqgX%2FDU0H0ie07xad3MwdHI8FZtQVGFZJxOyBDKc%2B&amp;nvMid=8095458474&amp;catId=50011943">판매처
                                <!-- -->1,083</a></strong></div>
                    <div class="basicList_depth__SbZWF"><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">식품</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">통조림/캔</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">햄</span></div>
                    <div class="basicList_desc__3kwkT">
                        <div class="basicList_detail_box__OoXKt"><a class="basicList_detail__8kFi2" rel="noopener"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#">보관방법 : 실온보관</a><a
                                class="basicList_detail__8kFi2 basicList_bar__XiBn4" rel="noopener"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#">용도 : 가정용</a><a
                                class="basicList_detail__8kFi2 basicList_bar__XiBn4" rel="noopener"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#">중량 : 340g</a><a
                                class="basicList_detail__8kFi2 basicList_bar__XiBn4" rel="noopener"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#">개당열량 :
                                1037kcal</a></div>
                        <div class="basicList_product_event__5pRAq"></div>
                    </div>
                    <div class="basicList_etc_box__5lkgg"><a target="_blank" class="basicList_etc__LSkN_" rel="noopener"
                            data-nclick="N=a:lst*C.comment,r:1,i:8095458474"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=VsSEXKPY3svzWhnLzbeaVP%2F%2F%2Fw%3D%3DsU1laCgPkdbAROgZdao2X3E01hKsiLLwwg2BmG%2B44QCi9OhgEgWOYg6VLdD%2F7t%2Fdm4RwYAVs%2FBoYH1JBycUa7ZFsZOinTopHxyAyK2u%2FTy%2BjYsfDmngMDc30arSUbghlw8ss4UymE29LknfqYKBhSB5VKLZjQ%2Fw6mGkjrCQya8BrxE5wD2k%2BOpsDqih5IlyNuy%2F6MHZ6u%2F5n6uuzlUc6JNCAYTv5lq0qN%2FmER%2FVdy2QpvuzH7jETdzdbLBEPy40zwub7oD2b6ZN0ODOADdG4X%2FfDsptBh%2F1SQMJZ67RBmboz84irqoupb5cHtoCFQH9lAJV03cukp%2F9sq6JmLvPVclMbjHM9FLNozUIiMWIsXiRwJ3LjRY%2BIkNjZ%2BdiRsKM%2FX0PXurd6BwFrLIufN4yO47dfcgDZbX1uPBgtMBVpOy7Ql0VMPq%2BhwUasLr5wH1EqZSHOsd6oOv8c9AQXdJvlpsKIH%2B1DZs0Gn3b3sxU%2FrvBOYx3ImiOU50eGhoT8AXjXfW3zfdWk0su43MKqtVvUP3UKlLqqrZpAXMAk1bBVmM7BW1Ik0iksMHUM%2B%2FBfeOdoyP4QSzZ0OitoLsmEMWvjVV95ZqgX%2FDU0H0ie07xad3MwdHI8FZtQVGFZJxOyBDKc%2B&amp;nvMid=8095458474&amp;catId=50011943">리뷰<span
                                class="basicList_graph__fzzbR"><span style="width:96%" class="basicList_star__UzKiv">별점
                                    <!-- -->4.8</span></span><em class="basicList_num__sfz3h">19,558</em></a><span
                            class="basicList_etc__LSkN_">등록일 <!-- -->2014.11.</span><span
                            class="basicList_etc__LSkN_"><a href="#" role="button"
                                class="basicList_btn_zzim__YCRGy N=a:lst*C.mylist,i:8095458474,r:1"
                                data-nclick="N=a:lst*C.mylist,i:8095458474,r:1" data-i="8095458474"
                                data-testid="ZZIM_BUTTON"><svg width="16" height="14" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="basicList_svg_zzim__rw2qP">
                                    <path
                                        d="M6.812 2.02a3.345 3.345 0 00-4.81 0C.665 3.381.665 5.601 2 6.966L7.988 13l6.179-6.224c1.167-1.355 1.105-3.455-.168-4.756A3.337 3.337 0 0011.594 1c-.91 0-1.764.361-2.407 1.02L6.543 4.692a1.7 1.7 0 000 2.424c.676.67 1.778.67 2.456 0l2.577-2.594"
                                        stroke="currentcolor"></path>
                                </svg><span class="basicList_text__gCaiD">찜하기<em
                                        class="basicList_num__sfz3h">239</em></span></a></span><span
                            class="basicList_etc__LSkN_"><a href="#" class="report_link_report__pkIEk"
                                data-nclick="N=a:lst*C.report,i:8095458474,r:1" data-testid="SEARCH_PRODUCT_REPORT"><svg
                                    width="14" height="14" fill="none" xmlns="http://www.w3.org/2000/svg"
                                    class="report_svg_report__xPbmh">
                                    <path clip-rule="evenodd" d="M6.999 1A4.999 4.999 0 002 6v4h10V6a5 5 0 00-5.001-5z"
                                        stroke="#999" stroke-linejoin="round"></path>
                                    <path d="M6.5 3.5a2 2 0 00-2 2" stroke="#999"></path>
                                    <path clip-rule="evenodd" d="M1 13h12v-3H1v3z" stroke="#999"></path>
                                </svg>정보 수정요청</a></span></div>
                </div>
                <div class="basicList_mall_area__faH62">
                    <div class="basicList_mall_title__FDXX5"><a target="_blank" rel="noopener"
                            data-nclick="N=a:lst*C.bcatalog,i:8095458474,r:1"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=VsSEXKPY3svzWhnLzbeaVP%2F%2F%2Fw%3D%3DsU1laCgPkdbAROgZdao2X3E01hKsiLLwwg2BmG%2B44QCi9OhgEgWOYg6VLdD%2F7t%2Fdm4RwYAVs%2FBoYH1JBycUa7ZFsZOinTopHxyAyK2u%2FTy%2BjYsfDmngMDc30arSUbghlw8ss4UymE29LknfqYKBhSB5VKLZjQ%2Fw6mGkjrCQya8BrxE5wD2k%2BOpsDqih5IlyNuy%2F6MHZ6u%2F5n6uuzlUc6JNCAYTv5lq0qN%2FmER%2FVdy2QpvuzH7jETdzdbLBEPy40zwub7oD2b6ZN0ODOADdG4X%2FfDsptBh%2F1SQMJZ67RBmboz84irqoupb5cHtoCFQH9lAJV03cukp%2F9sq6JmLvPVclMbjHM9FLNozUIiMWIsXiRwJ3LjRY%2BIkNjZ%2BdiRsKM%2FX0PXurd6BwFrLIufN4yO47dfcgDZbX1uPBgtMBVpOy7Ql0VMPq%2BhwUasLr5wH1EqZSHOsd6oOv8c9AQXdJvlpsKIH%2B1DZs0Gn3b3sxU%2FrvBOYx3ImiOU50eGhoT8AXjXfW3zfdWk0su43MKqtVvUP3UKlLqqrZpAXMAk1bBVmM7BW1Ik0iksMHUM%2B%2FBfeOdoyP4QSzZ0OitoLsmEMWvjVV95ZqgX%2FDU0H0ie07xad3MwdHI8FZtQVGFZJxOyBDKc%2B&amp;nvMid=8095458474&amp;catId=50011943"><em
                                class="basicList_brand__zeEQD">브랜드 카탈로그</em></a></div>
                    <ul class="basicList_mall_list__S_B5C">
                        <li data-nclick="N=a:lst*C.plwbuy,i:8095458474,r:1"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="만물상품점"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span
                                        class="basicList_mall_name__XQlSa">만물상품점</span><span
                                        class="basicList_ico_cell___WKUY"><span class="basicList_ico_pay__NMZTL"><span
                                                class="n_npay_info__xZATR"><span class="n_npay_icon__DxpI2"
                                                    data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                                        class="blind">네이버플러스멤버십</span><svg
                                                        xmlns="http://www.w3.org/2000/svg" width="42" height="13"
                                                        viewBox="0 0 42 13">
                                                        <g fill="none" fill-rule="evenodd">
                                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                                            </path>
                                                            <path fill="#03C75A"
                                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                                            </path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path fill="#03C75A" fill-rule="nonzero"
                                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                                            </path>
                                                        </g>
                                                    </svg></span></span></span></span></span><span
                                    class="basicList_price__euNoD" data-testid="SEARCH_PRODUCT_PRICE_PER_MALL"><span
                                        class="basicList_ico_low__jDHgE"></span>2,900</span></a></li>
                        <li data-nclick="N=a:lst*C.plwbuy,i:8095458474,r:1"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="솔깃유통"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span
                                        class="basicList_mall_name__XQlSa">솔깃유통</span><span
                                        class="basicList_ico_cell___WKUY"><span class="basicList_ico_pay__NMZTL"><span
                                                class="n_npay_info__xZATR"><span class="n_npay_icon__DxpI2"
                                                    data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                                        class="blind">네이버플러스멤버십</span><svg
                                                        xmlns="http://www.w3.org/2000/svg" width="42" height="13"
                                                        viewBox="0 0 42 13">
                                                        <g fill="none" fill-rule="evenodd">
                                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                                            </path>
                                                            <path fill="#03C75A"
                                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                                            </path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path fill="#03C75A" fill-rule="nonzero"
                                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                                            </path>
                                                        </g>
                                                    </svg></span></span></span></span></span><span
                                    class="basicList_price__euNoD"
                                    data-testid="SEARCH_PRODUCT_PRICE_PER_MALL">3,490</span></a></li>
                        <li data-nclick="N=a:lst*C.plwbuy,i:8095458474,r:1"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="플랜 88"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span class="basicList_mall_name__XQlSa">플랜
                                        88</span><span class="basicList_ico_cell___WKUY"><span
                                            class="basicList_ico_pay__NMZTL"><span class="n_npay_info__xZATR"><span
                                                    class="n_npay_icon__DxpI2"
                                                    data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                                        class="blind">네이버플러스멤버십</span><svg
                                                        xmlns="http://www.w3.org/2000/svg" width="42" height="13"
                                                        viewBox="0 0 42 13">
                                                        <g fill="none" fill-rule="evenodd">
                                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                                            </path>
                                                            <path fill="#03C75A"
                                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                                            </path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path fill="#03C75A" fill-rule="nonzero"
                                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                                            </path>
                                                        </g>
                                                    </svg></span></span></span></span></span><span
                                    class="basicList_price__euNoD"
                                    data-testid="SEARCH_PRODUCT_PRICE_PER_MALL">3,550</span></a></li>
                        <li data-nclick="N=a:lst*C.plwbuy,i:8095458474,r:1"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="코스트코구매대행 몽땅365"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span class="basicList_mall_name__XQlSa">코스트코구매대행
                                        몽땅365</span><span class="basicList_ico_cell___WKUY"><span
                                            class="basicList_ico_pay__NMZTL"><span class="n_npay_info__xZATR"><span
                                                    class="n_npay_icon__DxpI2"
                                                    data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                                        class="blind">네이버플러스멤버십</span><svg
                                                        xmlns="http://www.w3.org/2000/svg" width="42" height="13"
                                                        viewBox="0 0 42 13">
                                                        <g fill="none" fill-rule="evenodd">
                                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                                            </path>
                                                            <path fill="#03C75A"
                                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                                            </path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path fill="#03C75A" fill-rule="nonzero"
                                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                                            </path>
                                                        </g>
                                                    </svg></span></span></span></span></span><span
                                    class="basicList_price__euNoD"
                                    data-testid="SEARCH_PRODUCT_PRICE_PER_MALL">3,550</span></a></li>
                        <li data-nclick="N=a:lst*C.plwbuy,i:8095458474,r:1"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="유니콘 마트"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span class="basicList_mall_name__XQlSa">유니콘
                                        마트</span><span class="basicList_ico_cell___WKUY"><span
                                            class="basicList_ico_pay__NMZTL"><span class="n_npay_info__xZATR"><span
                                                    class="n_npay_icon__DxpI2"
                                                    data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                                        class="blind">네이버플러스멤버십</span><svg
                                                        xmlns="http://www.w3.org/2000/svg" width="42" height="13"
                                                        viewBox="0 0 42 13">
                                                        <g fill="none" fill-rule="evenodd">
                                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                                            </path>
                                                            <path fill="#03C75A"
                                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                                            </path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path fill="#03C75A" fill-rule="nonzero"
                                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                                            </path>
                                                        </g>
                                                    </svg></span></span></span></span></span><span
                                    class="basicList_price__euNoD"
                                    data-testid="SEARCH_PRODUCT_PRICE_PER_MALL">3,550</span></a></li>
                    </ul>
                </div>
            </div>
            <div class="basicList_info_option__JQ3EM">
                <ul class="basicList_list_option__3Z9wN">
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=BwmQzh0qiiWEwWaZUanf4v%2F%2F%2Fw%3D%3Ds2JiL9J1Wy00Vps1w2v0OcrMp29%2BShMDI%2B%2FAKpBY%2FuZ3D0AWU%2FasSPLGnk44ZiSgXMlxha6dJkDdojd1n8yfZClih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G6FnaNRNBkbe60z7QAaToBRdNmqsSj6uP7sF%2FvgTe%2F%2FUve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs5%2BoRu7h02xqr%2F41OTsRhBf6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqZ8%2BQbGUfCBHRMRDnxwXOqT1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCfJvpZ9A1JifOO0GEJOrLmKAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4DZeeeqGltGNEMt%2Bku5xrlm4gR%2F3KVH5%2Bfv0sl9RMeteHexdK3bHLOy7h%2Fx3cy1o6AYTYOqTv%2FsOm0kcFv3bjpJye2tAea4Ec%2B%2BUyYBPbm8fpTa%2BlleFwLta358irnpO9A35CyMrpXQUt3%2FJvHupy5s1ITc7NlRPvorKrNyQBKaY%3D&amp;nvMid=8095458474&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">1개</em></a><span class="basicList_price__euNoD">2,460원
                            (100g당 723원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=BwmQzh0qiiWEwWaZUanf4v%2F%2F%2Fw%3D%3Ds2JiL9J1Wy00Vps1w2v0OcrMp29%2BShMDI%2B%2FAKpBY%2FuZ3D0AWU%2FasSPLGnk44ZiSgXMlxha6dJkDdojd1n8yfZClih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G6FnaNRNBkbe60z7QAaToBRdNmqsSj6uP7sF%2FvgTe%2F%2FUve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs5%2BoRu7h02xqr%2F41OTsRhBf6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqZ8%2BQbGUfCBHRMRDnxwXOqT1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCfJvpZ9A1JifOO0GEJOrLmKAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4DZeeeqGltGNEMt%2Bku5xrlm4gR%2F3KVH5%2Bfv0sl9RMeteHexdK3bHLOy7h%2Fx3cy1o6AYTYOqTv%2FsOm0kcFv3bjpJye2tAea4Ec%2B%2BUyYBPbm8fpTa%2BlleFwLta358irnpO9A35CyMrpXQUt3%2FJvHupy5s1ITc7NlRPvorKrNyQBKaY%3D&amp;nvMid=8095458474&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">236<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=l31%2Fkji4QVtP3HW99fLeh%2F%2F%2F%2Fw%3D%3DsSEefo5rgrnG1ix9PbO0tX7Mp29%2BShMDI%2B%2FAKpBY%2FuZ0n%2Fli1Pj%2FCBVcFqHr%2FIQAo2NCJpPsnZPly2Q1Js3gfr1ih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G6FnaNRNBkbe60z7QAaToBRdNmqsSj6uP7sF%2FvgTe%2F%2FUve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs7%2FkZSEzwAtcMISBGQfvzsF6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqBoNdSl2h6UYs8pxcpqIK7T1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCfJvpZ9A1JifOO0GEJOrLmKAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4DZeeeqGltGNEMt%2Bku5xrlm4gR%2F3KVH5%2Bfv0sl9RMeteHexdK3bHLOy7h%2Fx3cy1o6AYTYOqTv%2FsOm0kcFv3bjpJye2tAea4Ec%2B%2BUyYBPbm8fpTa%2BlleFwLta358irnpO9A35CyMrpXQUt3%2FJvHupy5s1ITc7NlRPvorKrNyQBKaY%3D&amp;nvMid=8095458474&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">2개</em></a><span class="basicList_price__euNoD">7,340원
                            (100g당 1,079원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=l31%2Fkji4QVtP3HW99fLeh%2F%2F%2F%2Fw%3D%3DsSEefo5rgrnG1ix9PbO0tX7Mp29%2BShMDI%2B%2FAKpBY%2FuZ0n%2Fli1Pj%2FCBVcFqHr%2FIQAo2NCJpPsnZPly2Q1Js3gfr1ih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G6FnaNRNBkbe60z7QAaToBRdNmqsSj6uP7sF%2FvgTe%2F%2FUve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs7%2FkZSEzwAtcMISBGQfvzsF6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqBoNdSl2h6UYs8pxcpqIK7T1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCfJvpZ9A1JifOO0GEJOrLmKAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4DZeeeqGltGNEMt%2Bku5xrlm4gR%2F3KVH5%2Bfv0sl9RMeteHexdK3bHLOy7h%2Fx3cy1o6AYTYOqTv%2FsOm0kcFv3bjpJye2tAea4Ec%2B%2BUyYBPbm8fpTa%2BlleFwLta358irnpO9A35CyMrpXQUt3%2FJvHupy5s1ITc7NlRPvorKrNyQBKaY%3D&amp;nvMid=8095458474&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">70<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=t1zqtibI9kIp6W8FNBNCT%2F%2F%2F%2Fw%3D%3Ds%2FzwYtrKwTtZxZCF%2Bb6BAJ2clbLL2NuiiqDoGsPeuzsQ1vZayOtQkNQKbsv%2B%2BueVZwO6LypeD2%2BQV8jv0NTdtfGIQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYbSh73T1I%2FbO5EBT7kJuSvZcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykYc%2FpSSBTOdFAyqouKV6FsY5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpuIP6Skmh9NY0a4sKeNyri42kk5q1Yz7NTNs9zu80WqLcCnIaWQZiGDpSIRmj9VowrpFeYsUm03JwWCFF2ENX2m4Jfup8rDe4spUk8vsQQKEPQ431u6w0VnGxRIDS8%2FMJlQCjvuguHfszlgVjHJ1EN9U6l34n%2BhExTwz7mP9tOnNk%2FTtcr971X7DYYMYbjZHUwtIYh35n85gCNF9XAudNitgCgu8TH6IETI9IR%2BJIKXfrcnRhZzbAN7SHzzhZd3R0zdtBweXd5cMdZaF%2FiZ04hQau4fTwOUqyF63FjwpQRls%3D&amp;nvMid=8095458474&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">3개</em></a><span class="basicList_price__euNoD">11,000원
                            (100g당 1,078원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=t1zqtibI9kIp6W8FNBNCT%2F%2F%2F%2Fw%3D%3Ds%2FzwYtrKwTtZxZCF%2Bb6BAJ2clbLL2NuiiqDoGsPeuzsQ1vZayOtQkNQKbsv%2B%2BueVZwO6LypeD2%2BQV8jv0NTdtfGIQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYbSh73T1I%2FbO5EBT7kJuSvZcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykYc%2FpSSBTOdFAyqouKV6FsY5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpuIP6Skmh9NY0a4sKeNyri42kk5q1Yz7NTNs9zu80WqLcCnIaWQZiGDpSIRmj9VowrpFeYsUm03JwWCFF2ENX2m4Jfup8rDe4spUk8vsQQKEPQ431u6w0VnGxRIDS8%2FMJlQCjvuguHfszlgVjHJ1EN9U6l34n%2BhExTwz7mP9tOnNk%2FTtcr971X7DYYMYbjZHUwtIYh35n85gCNF9XAudNitgCgu8TH6IETI9IR%2BJIKXfrcnRhZzbAN7SHzzhZd3R0zdtBweXd5cMdZaF%2FiZ04hQau4fTwOUqyF63FjwpQRls%3D&amp;nvMid=8095458474&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">36<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=UlDrp4Kxuo7XOJY1Ka%2FArv%2F%2F%2Fw%3D%3DsJBovfTjWmURJOk9HzG6F9%2FrsPw%2FyOcnoc%2FXx6V%2FH%2FQcIs8PI%2FXkNBelkI5qp%2BcdUNkVRwJEayzEsTrAN8W5fDvK5o%2BRZGDibGWabTPYDtA9T5JDDNhynOBZEiIQFfYx030%2BAGAkSXtSmNrH2cOFPqusyPdtj2%2B7y0Uoslru8TzwXvcHdAkh2w2B%2BGiqrLfePgGwmPNX%2Fe%2BXkuZ30duRQYsacRzM6vfAD0Qmg6Zg6oZ7AAzvACjHKJy7j4OS8mQfCqqVi8UZf2pAJMXEkGpNLUTJ7MGmckokq1mnNNIGvwMD5LzR1ItMUfWhNOGHDv0vaO6d4y61HSQtdrbVfABLvsIBsJjzV%2F3vl5Lmd9HbkUGI%2FzdYC%2FwYAihDQzAs9Z5v9aXNPhUHnVgW08E65vp%2F%2FwhWNAKkiTmTHiwlbaGtF%2BcpOtX%2FkoYP81GsKFV4Fm0nFWXM1n34rUB4ev73ABnp2Zpw9%2FDMX2S1ZzF2txO07wpRJ48RU%2F5aIj2BAXR7TvP3Iw5ws8YXKa%2Bzyzckgr9rttgMV748%2FUQzRQh8aciUs3OMPUEjDw1yWsAMzROeVZspoiA3%2FU2AzguC84AnoS7Lq%2BYffpx3Lrf0Io%2BjHGIf5AaStOpg7YSTvszkq42o7yenc5Hv1T%2FoDPeAT2ZD%2BWCfnsQ%3D%3D&amp;nvMid=8095458474&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">4개</em></a><span class="basicList_price__euNoD">14,800원
                            (100g당 1,088원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=UlDrp4Kxuo7XOJY1Ka%2FArv%2F%2F%2Fw%3D%3DsJBovfTjWmURJOk9HzG6F9%2FrsPw%2FyOcnoc%2FXx6V%2FH%2FQcIs8PI%2FXkNBelkI5qp%2BcdUNkVRwJEayzEsTrAN8W5fDvK5o%2BRZGDibGWabTPYDtA9T5JDDNhynOBZEiIQFfYx030%2BAGAkSXtSmNrH2cOFPqusyPdtj2%2B7y0Uoslru8TzwXvcHdAkh2w2B%2BGiqrLfePgGwmPNX%2Fe%2BXkuZ30duRQYsacRzM6vfAD0Qmg6Zg6oZ7AAzvACjHKJy7j4OS8mQfCqqVi8UZf2pAJMXEkGpNLUTJ7MGmckokq1mnNNIGvwMD5LzR1ItMUfWhNOGHDv0vaO6d4y61HSQtdrbVfABLvsIBsJjzV%2F3vl5Lmd9HbkUGI%2FzdYC%2FwYAihDQzAs9Z5v9aXNPhUHnVgW08E65vp%2F%2FwhWNAKkiTmTHiwlbaGtF%2BcpOtX%2FkoYP81GsKFV4Fm0nFWXM1n34rUB4ev73ABnp2Zpw9%2FDMX2S1ZzF2txO07wpRJ48RU%2F5aIj2BAXR7TvP3Iw5ws8YXKa%2Bzyzckgr9rttgMV748%2FUQzRQh8aciUs3OMPUEjDw1yWsAMzROeVZspoiA3%2FU2AzguC84AnoS7Lq%2BYffpx3Lrf0Io%2BjHGIf5AaStOpg7YSTvszkq42o7yenc5Hv1T%2FoDPeAT2ZD%2BWCfnsQ%3D%3D&amp;nvMid=8095458474&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">30<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=6Dwm3WTmXRIhRD3yGA6cjP%2F%2F%2Fw%3D%3Dsyywo2CQhds568gIhzhq0K7Mp29%2BShMDI%2B%2FAKpBY%2FuZ3Paiyx5X551Z8SfL8Uv3yrGe2c8%2F3ihrVE0zXqG%2BUN3lih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G6FnaNRNBkbe60z7QAaToBRdNmqsSj6uP7sF%2FvgTe%2F%2FUve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs5mhSs78HNUlEIa3HLj7F7n6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqNThCYCPjbsdhaAqmzkrmpD1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCfJvpZ9A1JifOO0GEJOrLmKAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4DZeeeqGltGNEMt%2Bku5xrlm4gR%2F3KVH5%2Bfv0sl9RMeteHexdK3bHLOy7h%2Fx3cy1o6AYTYOqTv%2FsOm0kcFv3bjpJye2tAea4Ec%2B%2BUyYBPbm8fpTa%2BlleFwLta358irnpO9A35CyMrpXQUt3%2FJvHupy5s1ITc7NlRPvorKrNyQBKaY%3D&amp;nvMid=8095458474&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">5개</em></a><span class="basicList_price__euNoD">18,310원
                            (100g당 1,077원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=6Dwm3WTmXRIhRD3yGA6cjP%2F%2F%2Fw%3D%3Dsyywo2CQhds568gIhzhq0K7Mp29%2BShMDI%2B%2FAKpBY%2FuZ3Paiyx5X551Z8SfL8Uv3yrGe2c8%2F3ihrVE0zXqG%2BUN3lih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G6FnaNRNBkbe60z7QAaToBRdNmqsSj6uP7sF%2FvgTe%2F%2FUve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs5mhSs78HNUlEIa3HLj7F7n6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqNThCYCPjbsdhaAqmzkrmpD1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCfJvpZ9A1JifOO0GEJOrLmKAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4DZeeeqGltGNEMt%2Bku5xrlm4gR%2F3KVH5%2Bfv0sl9RMeteHexdK3bHLOy7h%2Fx3cy1o6AYTYOqTv%2FsOm0kcFv3bjpJye2tAea4Ec%2B%2BUyYBPbm8fpTa%2BlleFwLta358irnpO9A35CyMrpXQUt3%2FJvHupy5s1ITc7NlRPvorKrNyQBKaY%3D&amp;nvMid=8095458474&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">49<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=u8JPhgGN3UeRiQEJGiAWGP%2F%2F%2Fw%3D%3Ds3FgvvXLi4uVCqgGKHDDMmGclbLL2NuiiqDoGsPeuzsQ1vZayOtQkNQKbsv%2B%2BueVZjrLRzRe8x%2BbinQ%2BkPNOxO2IQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYbSh73T1I%2FbO5EBT7kJuSvZcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykauOjR4mIJazOXIFaauUKD%2F5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpvhlOwxaIcKFHgAYW8Y28CHGAf3icibIgTAtGFsYvOSXcCnIaWQZiGDpSIRmj9VowrpFeYsUm03JwWCFF2ENX2m4Jfup8rDe4spUk8vsQQKEPQ431u6w0VnGxRIDS8%2FMJlQCjvuguHfszlgVjHJ1EN9U6l34n%2BhExTwz7mP9tOnNk%2FTtcr971X7DYYMYbjZHUwtIYh35n85gCNF9XAudNitgCgu8TH6IETI9IR%2BJIKXfrcnRhZzbAN7SHzzhZd3R0zdtBweXd5cMdZaF%2FiZ04hQau4fTwOUqyF63FjwpQRls%3D&amp;nvMid=8095458474&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">6개</em></a><span class="basicList_price__euNoD">22,310원
                            (100g당 1,093원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=u8JPhgGN3UeRiQEJGiAWGP%2F%2F%2Fw%3D%3Ds3FgvvXLi4uVCqgGKHDDMmGclbLL2NuiiqDoGsPeuzsQ1vZayOtQkNQKbsv%2B%2BueVZjrLRzRe8x%2BbinQ%2BkPNOxO2IQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYbSh73T1I%2FbO5EBT7kJuSvZcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykauOjR4mIJazOXIFaauUKD%2F5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpvhlOwxaIcKFHgAYW8Y28CHGAf3icibIgTAtGFsYvOSXcCnIaWQZiGDpSIRmj9VowrpFeYsUm03JwWCFF2ENX2m4Jfup8rDe4spUk8vsQQKEPQ431u6w0VnGxRIDS8%2FMJlQCjvuguHfszlgVjHJ1EN9U6l34n%2BhExTwz7mP9tOnNk%2FTtcr971X7DYYMYbjZHUwtIYh35n85gCNF9XAudNitgCgu8TH6IETI9IR%2BJIKXfrcnRhZzbAN7SHzzhZd3R0zdtBweXd5cMdZaF%2FiZ04hQau4fTwOUqyF63FjwpQRls%3D&amp;nvMid=8095458474&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">109<!-- -->개</span></a></li>
                </ul><a target="_blank" class="basicList_link_more_option__73RUB" rel="noopener"
                    data-nclick="N=a:lst*C.conmore"
                    href="https://cr.shopping.naver.com/adcr.nhn?x=5g68SxRYiRWB0NVK0h6zX%2F%2F%2F%2Fw%3D%3DsHEtnGezy3Jy8n4PvHzySRbMp29%2BShMDI%2B%2FAKpBY%2FuZ0qCGnoCg4de%2F210PorrWe8uyXYcCmZLUmq17LowoADKFih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G6FnaNRNBkbe60z7QAaToBRdNmqsSj6uP7sF%2FvgTe%2F%2FUve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs7mDA6ms801Q5f3S%2FAFj6Z4Q%2BD%2Fo9glb0ukJK6bM8miKArsK1DNlYuW6vX8WB7j4SmKvQdOa3%2FzlERLTdM%2FqiFYnLCZ%2BPw10CFqc0KKaGV%2B11OSD8q2VMoDmI3bAmd6ZdybMZwOzBAZXiQT8tDZvqpCLpTEl5qHQ6bSWQg5m1P1kiD9D0f8VwU9MZjSmaSmGD5KyQJIbdfCrxRgSEbHndafNg5XjYPuL3E%2BAtNvCz0eQ%2B3ChVqx7w6nEd9xys1WcpRP4PMPHCnudPTZjGRUD3iURnRm%2B4ETj6EtlaSATui%2FvG8y9%2FWeqnhIVTGC8%2FEz9FIBNCgGhnJoYyA8V4j2ARcNDVCYCaeglF2rgr1u2OQIzQ%3D%3D&amp;nvMid=8095458474&amp;catId=50011943">옵션
                    더보기</a>
            </div>
        </li>
    </div>
    <div>
        <li class="basicList_item__0T9JD">
            <div class="basicList_inner__xCM3J">
                <div class="basicList_img_area__AdRY_">
                    <div class="thumbnail_thumb_wrap__RbcYO _wrapper"><a target="_blank" class="thumbnail_thumb__Bxb6Z"
                            rel="noopener" data-nclick="N=a:lst*C.image,r:2,i:5786210213" data-testid="SEARCH_PRODUCT"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=g4AuE9qjCyMKDDiJN%2B1jfP%2F%2F%2Fw%3D%3Dsokx5%2FnYNNMgh7NMT4Ji24JoxmEr%2BgBPkq0FYQTBci424IGggYhMjUGLogy1H2BatVf6Su9iRFHehhZ%2Fw%2BzMZF2g6HabDTRx466CGciRiUnFBZuMfzSBinsMMtj7lqMfUgEH7aWDLlHhTauUFK%2BE8pqzUR4Sl8xBhuF2vuaKqBwcPBCP8AviRbjo74P5aaPgG334rL%2BbR36BhYe0R%2FrUmjkI1yUrC8vID%2FKz%2F8c89qMv0%2B7VqFzcMM74gAFJ7zCJQEq7zZ3E6b0%2BNG8RqJmG9tWuM4lftPB0WTqHoHh3cU7fbLWo5y0EVpxpTjpbff6SoB7P9jx5KZr1oy9qstZx7m0QIc6YJa575QRppSEcyLocPqIDov7I7ZZGnXbJmCS%2FMZCKbS5IZXjkbKBm9wVCukCuRkUVEtfumYieI8%2F6zLRsUdsTe2HlZlP6fuu9JMo3iRYgXT8U0rr2Dm%2BuxQGAQBp3JhyNfyBiQ%2F3cTMbviC2HyNHyBUXwWVD2ki0TxnNzyrm6lxhxDQFXTL%2BVZ2vOHMAjEKd3JBIBNONewhOAHvNi%2FhgaMkJIhbUi8HFdPXAb3g1z34821bNEH2SO92GolkAbHXAbxCX3ZAPRzqXGsA%2FIOEsHC78VBLnFZh%2FnDobeN&amp;nvMid=5786210213&amp;catId=50011943"><img
                                width="140" height="140" alt="CJ제일제당 스팸 클래식 200g"
                                src="https://shopping-phinf.pstatic.net/main_5786210/5786210213.20210826105937.jpg?type=f140"></a>
                        <div class="thumbnail_btn_box____IiP">
                            <div class="thumbnail_btn__3Gjg1"><button type="button" class="thumbnail_save__yu3R_"
                                    data-nclick="N=a:lst*C.put"><span
                                        class="thumbnail_layer_info__r_5dH">담기</span></button>
                                <div class="thumbnail_layer_info__r_5dH">
                                    <div class="thumbnail_link_box__fhsB8"><a href="#" class="thumbnail_link__i3ShY"
                                            data-nclick="N=a:lst*C.putblog">내 블로그에 담기</a><a href="#"
                                            class="thumbnail_link__i3ShY" data-nclick="N=a:lst*C.putcafe">카페에 담기</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="basicList_info_area__TWvzp">
                    <div class="basicList_title__VfX3c"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.title,i:5786210213,r:2" data-testid="SEARCH_PRODUCT"
                            title="CJ제일제당 스팸 클래식 200g"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=g4AuE9qjCyMKDDiJN%2B1jfP%2F%2F%2Fw%3D%3Dsokx5%2FnYNNMgh7NMT4Ji24JoxmEr%2BgBPkq0FYQTBci424IGggYhMjUGLogy1H2BatVf6Su9iRFHehhZ%2Fw%2BzMZF2g6HabDTRx466CGciRiUnFBZuMfzSBinsMMtj7lqMfUgEH7aWDLlHhTauUFK%2BE8pqzUR4Sl8xBhuF2vuaKqBwcPBCP8AviRbjo74P5aaPgG334rL%2BbR36BhYe0R%2FrUmjkI1yUrC8vID%2FKz%2F8c89qMv0%2B7VqFzcMM74gAFJ7zCJQEq7zZ3E6b0%2BNG8RqJmG9tWuM4lftPB0WTqHoHh3cU7fbLWo5y0EVpxpTjpbff6SoB7P9jx5KZr1oy9qstZx7m0QIc6YJa575QRppSEcyLocPqIDov7I7ZZGnXbJmCS%2FMZCKbS5IZXjkbKBm9wVCukCuRkUVEtfumYieI8%2F6zLRsUdsTe2HlZlP6fuu9JMo3iRYgXT8U0rr2Dm%2BuxQGAQBp3JhyNfyBiQ%2F3cTMbviC2HyNHyBUXwWVD2ki0TxnNzyrm6lxhxDQFXTL%2BVZ2vOHMAjEKd3JBIBNONewhOAHvNi%2FhgaMkJIhbUi8HFdPXAb3g1z34821bNEH2SO92GolkAbHXAbxCX3ZAPRzqXGsA%2FIOEsHC78VBLnFZh%2FnDobeN&amp;nvMid=5786210213&amp;catId=50011943">CJ제일제당
                            스팸 클래식 200g</a></div>
                    <div class="basicList_price_area__K7DDT"><strong class="basicList_price__euNoD"><span><span
                                    class="price_low__y_ZUj">최저</span><span class="price_num__S2p_v"
                                    data-testid="SEARCH_PRODUCT_PRICE">700원</span></span><a target="_blank"
                                class="basicList_compare__d2bWN" rel="noopener"
                                data-nclick="N=a:lst*C.compare,i:5786210213,r:2"
                                href="https://cr.shopping.naver.com/adcr.nhn?x=g4AuE9qjCyMKDDiJN%2B1jfP%2F%2F%2Fw%3D%3Dsokx5%2FnYNNMgh7NMT4Ji24JoxmEr%2BgBPkq0FYQTBci424IGggYhMjUGLogy1H2BatVf6Su9iRFHehhZ%2Fw%2BzMZF2g6HabDTRx466CGciRiUnFBZuMfzSBinsMMtj7lqMfUgEH7aWDLlHhTauUFK%2BE8pqzUR4Sl8xBhuF2vuaKqBwcPBCP8AviRbjo74P5aaPgG334rL%2BbR36BhYe0R%2FrUmjkI1yUrC8vID%2FKz%2F8c89qMv0%2B7VqFzcMM74gAFJ7zCJQEq7zZ3E6b0%2BNG8RqJmG9tWuM4lftPB0WTqHoHh3cU7fbLWo5y0EVpxpTjpbff6SoB7P9jx5KZr1oy9qstZx7m0QIc6YJa575QRppSEcyLocPqIDov7I7ZZGnXbJmCS%2FMZCKbS5IZXjkbKBm9wVCukCuRkUVEtfumYieI8%2F6zLRsUdsTe2HlZlP6fuu9JMo3iRYgXT8U0rr2Dm%2BuxQGAQBp3JhyNfyBiQ%2F3cTMbviC2HyNHyBUXwWVD2ki0TxnNzyrm6lxhxDQFXTL%2BVZ2vOHMAjEKd3JBIBNONewhOAHvNi%2FhgaMkJIhbUi8HFdPXAb3g1z34821bNEH2SO92GolkAbHXAbxCX3ZAPRzqXGsA%2FIOEsHC78VBLnFZh%2FnDobeN&amp;nvMid=5786210213&amp;catId=50011943">판매처
                                <!-- -->1,193</a></strong></div>
                    <div class="basicList_depth__SbZWF"><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">식품</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">통조림/캔</span><span
                            class="basicList_category__cXUaZ basicList_nohover__TJr2_">햄</span></div>
                    <div class="basicList_desc__3kwkT">
                        <div class="basicList_detail_box__OoXKt"><a class="basicList_detail__8kFi2" rel="noopener"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#">보관방법 : 실온보관</a><a
                                class="basicList_detail__8kFi2 basicList_bar__XiBn4" rel="noopener"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#">용도 : 가정용</a><a
                                class="basicList_detail__8kFi2 basicList_bar__XiBn4" rel="noopener"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#">중량 : 200g</a><a
                                class="basicList_detail__8kFi2 basicList_bar__XiBn4" rel="noopener"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#">개당열량 :
                                615kcal</a></div>
                        <div class="basicList_product_event__5pRAq"></div>
                    </div>
                    <div class="basicList_etc_box__5lkgg"><a target="_blank" class="basicList_etc__LSkN_" rel="noopener"
                            data-nclick="N=a:lst*C.comment,r:2,i:5786210213"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=g4AuE9qjCyMKDDiJN%2B1jfP%2F%2F%2Fw%3D%3Dsokx5%2FnYNNMgh7NMT4Ji24JoxmEr%2BgBPkq0FYQTBci424IGggYhMjUGLogy1H2BatVf6Su9iRFHehhZ%2Fw%2BzMZF2g6HabDTRx466CGciRiUnFBZuMfzSBinsMMtj7lqMfUgEH7aWDLlHhTauUFK%2BE8pqzUR4Sl8xBhuF2vuaKqBwcPBCP8AviRbjo74P5aaPgG334rL%2BbR36BhYe0R%2FrUmjkI1yUrC8vID%2FKz%2F8c89qMv0%2B7VqFzcMM74gAFJ7zCJQEq7zZ3E6b0%2BNG8RqJmG9tWuM4lftPB0WTqHoHh3cU7fbLWo5y0EVpxpTjpbff6SoB7P9jx5KZr1oy9qstZx7m0QIc6YJa575QRppSEcyLocPqIDov7I7ZZGnXbJmCS%2FMZCKbS5IZXjkbKBm9wVCukCuRkUVEtfumYieI8%2F6zLRsUdsTe2HlZlP6fuu9JMo3iRYgXT8U0rr2Dm%2BuxQGAQBp3JhyNfyBiQ%2F3cTMbviC2HyNHyBUXwWVD2ki0TxnNzyrm6lxhxDQFXTL%2BVZ2vOHMAjEKd3JBIBNONewhOAHvNi%2FhgaMkJIhbUi8HFdPXAb3g1z34821bNEH2SO92GolkAbHXAbxCX3ZAPRzqXGsA%2FIOEsHC78VBLnFZh%2FnDobeN&amp;nvMid=5786210213&amp;catId=50011943">리뷰<span
                                class="basicList_graph__fzzbR"><span style="width:98%" class="basicList_star__UzKiv">별점
                                    <!-- -->4.9</span></span><em class="basicList_num__sfz3h">38,627</em></a><span
                            class="basicList_etc__LSkN_">등록일 <!-- -->2011.06.</span><span
                            class="basicList_etc__LSkN_"><a href="#" role="button"
                                class="basicList_btn_zzim__YCRGy N=a:lst*C.mylist,i:5786210213,r:2"
                                data-nclick="N=a:lst*C.mylist,i:5786210213,r:2" data-i="5786210213"
                                data-testid="ZZIM_BUTTON"><svg width="16" height="14" fill="none"
                                    xmlns="http://www.w3.org/2000/svg" class="basicList_svg_zzim__rw2qP">
                                    <path
                                        d="M6.812 2.02a3.345 3.345 0 00-4.81 0C.665 3.381.665 5.601 2 6.966L7.988 13l6.179-6.224c1.167-1.355 1.105-3.455-.168-4.756A3.337 3.337 0 0011.594 1c-.91 0-1.764.361-2.407 1.02L6.543 4.692a1.7 1.7 0 000 2.424c.676.67 1.778.67 2.456 0l2.577-2.594"
                                        stroke="currentcolor"></path>
                                </svg><span class="basicList_text__gCaiD">찜하기<em
                                        class="basicList_num__sfz3h">290</em></span></a></span><span
                            class="basicList_etc__LSkN_"><a href="#" class="report_link_report__pkIEk"
                                data-nclick="N=a:lst*C.report,i:5786210213,r:2" data-testid="SEARCH_PRODUCT_REPORT"><svg
                                    width="14" height="14" fill="none" xmlns="http://www.w3.org/2000/svg"
                                    class="report_svg_report__xPbmh">
                                    <path clip-rule="evenodd" d="M6.999 1A4.999 4.999 0 002 6v4h10V6a5 5 0 00-5.001-5z"
                                        stroke="#999" stroke-linejoin="round"></path>
                                    <path d="M6.5 3.5a2 2 0 00-2 2" stroke="#999"></path>
                                    <path clip-rule="evenodd" d="M1 13h12v-3H1v3z" stroke="#999"></path>
                                </svg>정보 수정요청</a></span></div>
                </div>
                <div class="basicList_mall_area__faH62">
                    <div class="basicList_mall_title__FDXX5"><a target="_blank" rel="noopener"
                            data-nclick="N=a:lst*C.bcatalog,i:5786210213,r:2"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=g4AuE9qjCyMKDDiJN%2B1jfP%2F%2F%2Fw%3D%3Dsokx5%2FnYNNMgh7NMT4Ji24JoxmEr%2BgBPkq0FYQTBci424IGggYhMjUGLogy1H2BatVf6Su9iRFHehhZ%2Fw%2BzMZF2g6HabDTRx466CGciRiUnFBZuMfzSBinsMMtj7lqMfUgEH7aWDLlHhTauUFK%2BE8pqzUR4Sl8xBhuF2vuaKqBwcPBCP8AviRbjo74P5aaPgG334rL%2BbR36BhYe0R%2FrUmjkI1yUrC8vID%2FKz%2F8c89qMv0%2B7VqFzcMM74gAFJ7zCJQEq7zZ3E6b0%2BNG8RqJmG9tWuM4lftPB0WTqHoHh3cU7fbLWo5y0EVpxpTjpbff6SoB7P9jx5KZr1oy9qstZx7m0QIc6YJa575QRppSEcyLocPqIDov7I7ZZGnXbJmCS%2FMZCKbS5IZXjkbKBm9wVCukCuRkUVEtfumYieI8%2F6zLRsUdsTe2HlZlP6fuu9JMo3iRYgXT8U0rr2Dm%2BuxQGAQBp3JhyNfyBiQ%2F3cTMbviC2HyNHyBUXwWVD2ki0TxnNzyrm6lxhxDQFXTL%2BVZ2vOHMAjEKd3JBIBNONewhOAHvNi%2FhgaMkJIhbUi8HFdPXAb3g1z34821bNEH2SO92GolkAbHXAbxCX3ZAPRzqXGsA%2FIOEsHC78VBLnFZh%2FnDobeN&amp;nvMid=5786210213&amp;catId=50011943"><em
                                class="basicList_brand__zeEQD">브랜드 카탈로그</em></a></div>
                    <ul class="basicList_mall_list__S_B5C">
                        <li data-nclick="N=a:lst*C.plwbuy,i:5786210213,r:2"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="11번가"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span
                                        class="basicList_mall_name__XQlSa">11번가</span><span
                                        class="basicList_ico_cell___WKUY"></span></span><span
                                    class="basicList_price__euNoD" data-testid="SEARCH_PRODUCT_PRICE_PER_MALL"><span
                                        class="basicList_ico_low__jDHgE"></span>2,290</span></a></li>
                        <li data-nclick="N=a:lst*C.plwbuy,i:5786210213,r:2"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="몰빵몰닷컴"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span
                                        class="basicList_mall_name__XQlSa">몰빵몰닷컴</span><span
                                        class="basicList_ico_cell___WKUY"><span class="basicList_ico_pay__NMZTL"><span
                                                class="n_npay_info__xZATR"><span class="n_npay_icon__DxpI2"
                                                    data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                                        class="blind">네이버플러스멤버십</span><svg
                                                        xmlns="http://www.w3.org/2000/svg" width="42" height="13"
                                                        viewBox="0 0 42 13">
                                                        <g fill="none" fill-rule="evenodd">
                                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                                            </path>
                                                            <path fill="#03C75A"
                                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                                            </path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path fill="#03C75A" fill-rule="nonzero"
                                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                                            </path>
                                                        </g>
                                                    </svg></span></span></span></span></span><span
                                    class="basicList_price__euNoD"
                                    data-testid="SEARCH_PRODUCT_PRICE_PER_MALL">2,300</span></a></li>
                        <li data-nclick="N=a:lst*C.plwbuy,i:5786210213,r:2"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="미종합유통"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span
                                        class="basicList_mall_name__XQlSa">미종합유통</span><span
                                        class="basicList_ico_cell___WKUY"><span class="basicList_ico_pay__NMZTL"><span
                                                class="n_npay_info__xZATR"><span class="n_npay_icon__DxpI2"
                                                    data-testid="CATALOG_NAVERPAY_PLUS_ICON_IN_PRODUCT"><span
                                                        class="blind">네이버플러스멤버십</span><svg
                                                        xmlns="http://www.w3.org/2000/svg" width="42" height="13"
                                                        viewBox="0 0 42 13">
                                                        <g fill="none" fill-rule="evenodd">
                                                            <path fill="#1E9BF5" fill-rule="nonzero"
                                                                d="M40.733 0H29.59l-2.708 6.661L29.59 13h11.143c.479 0 .867-.388.867-.867V.867c0-.479-.388-.867-.867-.867z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M36.965 5.638L36.965 3.064 35.24 3.064 35.24 5.638 32.667 5.638 32.667 7.362 39.539 7.362 39.539 5.638zM35.249 7.59l-.01 2.346h1.724V8.85c0-.818-.866-1.26-1.714-1.26zM.966.966H12.033V12.033H.966z">
                                                            </path>
                                                            <path fill="#03C75A"
                                                                d="M7.58 3.467L7.58 6.499 5.33 3.467 3.467 3.467 3.467 9.532 5.419 9.532 5.419 6.499 7.669 9.532 9.532 9.532 9.532 3.467z">
                                                            </path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path d="M1.127 1.127H11.872V11.872H1.127z"></path>
                                                            <path fill="#03C75A" fill-rule="nonzero"
                                                                d="M0 .867v11.266c0 .479.388.867.867.867H29.59c.41 0 .743-.333.743-.743V.743c0-.41-.332-.743-.743-.743H.867C.388 0 0 .388 0 .867zm1.127 11.005V1.127h10.745v10.745H1.127z">
                                                            </path>
                                                            <path fill="#FFF" fill-rule="nonzero"
                                                                d="M14.585 3.125h2.169c.3-.007.601.035.889.124.225.069.433.185.609.341.158.144.28.323.355.523.078.209.117.43.115.654v.167c0 .228-.042.453-.123.666-.08.21-.208.397-.372.55-.18.164-.39.29-.619.371-.278.098-.572.146-.866.14h-1.148v2.211h-1.01V3.125zm1.021.853v1.825h1.012c.276.015.55-.051.79-.19.19-.125.287-.36.287-.694v-.144c.004-.134-.02-.267-.072-.39-.045-.1-.115-.185-.203-.249-.095-.063-.203-.105-.316-.123-.131-.026-.265-.038-.398-.036l-1.1.001zm5.063 4.959c-.473 0-.84-.108-1.1-.324-.265-.223-.41-.558-.39-.905v-.255c-.002-.168.026-.336.083-.495.057-.154.153-.29.279-.396.152-.123.327-.213.516-.264.255-.07.518-.102.781-.096h1.006v-.168c0-.271-.063-.466-.188-.585-.126-.119-.324-.179-.594-.18-.45 0-.887.155-1.238.439l-.495-.733c.238-.163.492-.3.758-.411.314-.127.651-.188.99-.18.24-.002.479.03.71.095.203.057.393.15.562.277.156.114.284.265.371.438.091.184.137.387.133.593v3.085h-.902l-.016-.54c-.046.1-.116.189-.203.258-.095.078-.2.143-.314.19-.12.052-.244.09-.372.117-.124.026-.25.04-.377.04zm1.172-1.954h-.98c-.267 0-.451.05-.555.152-.106.108-.162.255-.155.406v.096c-.006.13.051.255.154.335.13.09.288.133.447.124.408 0 .711-.098.908-.295.084-.077.14-.179.159-.29.018-.134.026-.269.025-.403l-.003-.125zm2.68-2.504l.99 3.245h.032l1.004-3.245h1.069L25.34 10.7l-.94-.327.566-1.443L23.4 4.48h1.12z">
                                                            </path>
                                                        </g>
                                                    </svg></span></span></span></span></span><span
                                    class="basicList_price__euNoD"
                                    data-testid="SEARCH_PRODUCT_PRICE_PER_MALL">2,330</span></a></li>
                        <li data-nclick="N=a:lst*C.plwbuy,i:5786210213,r:2"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="옥션"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span
                                        class="basicList_mall_name__XQlSa">옥션</span><span
                                        class="basicList_ico_cell___WKUY"></span></span><span
                                    class="basicList_price__euNoD"
                                    data-testid="SEARCH_PRODUCT_PRICE_PER_MALL">2,440</span></a></li>
                        <li data-nclick="N=a:lst*C.plwbuy,i:5786210213,r:2"><a class="basicList_mall_item__bFc5i"
                                data-testid="SEARCH_PRODUCT_PER_MALL" title="G마켓"
                                href="/search/all?query=%EC%8A%A4%ED%8C%B8&amp;bt=-1&amp;frm=NVSCPRO#"><span
                                    class="basicList_mall_info__thmaN"><span
                                        class="basicList_mall_name__XQlSa">G마켓</span><span
                                        class="basicList_ico_cell___WKUY"></span></span><span
                                    class="basicList_price__euNoD"
                                    data-testid="SEARCH_PRODUCT_PRICE_PER_MALL">2,440</span></a></li>
                    </ul>
                </div>
            </div>
            <div class="basicList_info_option__JQ3EM">
                <ul class="basicList_list_option__3Z9wN">
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=Y7hxnZoJmh0R7rGfTLhMRP%2F%2F%2Fw%3D%3DsQD35cEDEgaFgSkBrtntQPMuOlELMxoP6CndKThHZrp%2FFQZFgO26JUNq87T1LW7qbAmlCjb1aS%2FaNTKCcRnjE5Vih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G8kR2qiTwxn15XNEV6Vnkxhm1SuVApM1ivHjmEKy4cRSve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs5%2BoRu7h02xqr%2F41OTsRhBf6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqq5S4zavXmG2Qbfd3L%2BDNAj1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCoa9M66M0uUv9q8IQkdCjRqAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4xQWWJaYpXAP4ZGjGZViE%2FGov7tAU1fWckO6MZvpKmzrsYS74fNDjve9MbBz4TnvpnUpTzmQTeleeE0y%2Brv8xbHOTfGZF38nrH7KTZrXyIwBjrJZ%2BWc3awGxP156SzuWiVoWd0jB03C5aYq3HUc1IKtSSLJQZncWk8e8Ttfjz6Fs%3D&amp;nvMid=5786210213&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">1개</em></a><span class="basicList_price__euNoD">700원
                            (100g당 350원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=Y7hxnZoJmh0R7rGfTLhMRP%2F%2F%2Fw%3D%3DsQD35cEDEgaFgSkBrtntQPMuOlELMxoP6CndKThHZrp%2FFQZFgO26JUNq87T1LW7qbAmlCjb1aS%2FaNTKCcRnjE5Vih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G8kR2qiTwxn15XNEV6Vnkxhm1SuVApM1ivHjmEKy4cRSve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs5%2BoRu7h02xqr%2F41OTsRhBf6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqq5S4zavXmG2Qbfd3L%2BDNAj1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCoa9M66M0uUv9q8IQkdCjRqAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4xQWWJaYpXAP4ZGjGZViE%2FGov7tAU1fWckO6MZvpKmzrsYS74fNDjve9MbBz4TnvpnUpTzmQTeleeE0y%2Brv8xbHOTfGZF38nrH7KTZrXyIwBjrJZ%2BWc3awGxP156SzuWiVoWd0jB03C5aYq3HUc1IKtSSLJQZncWk8e8Ttfjz6Fs%3D&amp;nvMid=5786210213&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">223<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=2wK%2FIw%2BEk88n7RaFM9VImv%2F%2F%2Fw%3D%3Ds8G0l%2BDBmbhONkRjchHupIMuOlELMxoP6CndKThHZrp8Baau%2B6He85wKew1ccs%2B%2BMMCwoxgYf8gCeDQaWNT9vqVih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G8kR2qiTwxn15XNEV6Vnkxhm1SuVApM1ivHjmEKy4cRSve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs7%2FkZSEzwAtcMISBGQfvzsF6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqex9ghC6EoFvFySI%2Bm1VgFD1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCoa9M66M0uUv9q8IQkdCjRqAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4xQWWJaYpXAP4ZGjGZViE%2FGov7tAU1fWckO6MZvpKmzrsYS74fNDjve9MbBz4TnvpnUpTzmQTeleeE0y%2Brv8xbHOTfGZF38nrH7KTZrXyIwBjrJZ%2BWc3awGxP156SzuWiVoWd0jB03C5aYq3HUc1IKtSSLJQZncWk8e8Ttfjz6Fs%3D&amp;nvMid=5786210213&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">2개</em></a><span class="basicList_price__euNoD">4,950원
                            (100g당 1,237원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=2wK%2FIw%2BEk88n7RaFM9VImv%2F%2F%2Fw%3D%3Ds8G0l%2BDBmbhONkRjchHupIMuOlELMxoP6CndKThHZrp8Baau%2B6He85wKew1ccs%2B%2BMMCwoxgYf8gCeDQaWNT9vqVih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G8kR2qiTwxn15XNEV6Vnkxhm1SuVApM1ivHjmEKy4cRSve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs7%2FkZSEzwAtcMISBGQfvzsF6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqex9ghC6EoFvFySI%2Bm1VgFD1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCoa9M66M0uUv9q8IQkdCjRqAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4xQWWJaYpXAP4ZGjGZViE%2FGov7tAU1fWckO6MZvpKmzrsYS74fNDjve9MbBz4TnvpnUpTzmQTeleeE0y%2Brv8xbHOTfGZF38nrH7KTZrXyIwBjrJZ%2BWc3awGxP156SzuWiVoWd0jB03C5aYq3HUc1IKtSSLJQZncWk8e8Ttfjz6Fs%3D&amp;nvMid=5786210213&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">11<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=4Jv7unCuXQhqfscY1Q%2Fcwf%2F%2F%2Fw%3D%3DsRliPvkCCnzQjUNtBX6hx91uqckbMgGvSnDoCWhYV7K01vZayOtQkNQKbsv%2B%2BueVZqRBRQbz6idzch%2BGW6C7Ka2IQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYb7yfk%2FxAhqEougrb5pDHjWcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykYc%2FpSSBTOdFAyqouKV6FsY5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpSwLrMhKpyYVLmPl0rIdloWUmwiq6wbPK7zGxm7QsrPjcCnIaWQZiGDpSIRmj9VowuyT71yi9V6bHpQ977omK2D6FURihOvVNK6%2BarovFEXYPQ431u6w0VnGxRIDS8%2FMJpR7UVCZp3ws1%2FNie8p11LdU6l34n%2BhExTwz7mP9tOnPtdEjB4ZJtcjuxf2dnsyEXT%2BDzDxwp7nT02YxkVA94lBzjTcXwoVM8lrhL6igy83LXeZDJLMvq4TQHBwah2gKPnLywBF6TPdyrHi5pSyQkVg1QmAmnoJRdq4K9btjkCM0%3D&amp;nvMid=5786210213&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">3개</em></a><span class="basicList_price__euNoD">7,400원
                            (100g당 1,233원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=4Jv7unCuXQhqfscY1Q%2Fcwf%2F%2F%2Fw%3D%3DsRliPvkCCnzQjUNtBX6hx91uqckbMgGvSnDoCWhYV7K01vZayOtQkNQKbsv%2B%2BueVZqRBRQbz6idzch%2BGW6C7Ka2IQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYb7yfk%2FxAhqEougrb5pDHjWcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykYc%2FpSSBTOdFAyqouKV6FsY5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpSwLrMhKpyYVLmPl0rIdloWUmwiq6wbPK7zGxm7QsrPjcCnIaWQZiGDpSIRmj9VowuyT71yi9V6bHpQ977omK2D6FURihOvVNK6%2BarovFEXYPQ431u6w0VnGxRIDS8%2FMJpR7UVCZp3ws1%2FNie8p11LdU6l34n%2BhExTwz7mP9tOnPtdEjB4ZJtcjuxf2dnsyEXT%2BDzDxwp7nT02YxkVA94lBzjTcXwoVM8lrhL6igy83LXeZDJLMvq4TQHBwah2gKPnLywBF6TPdyrHi5pSyQkVg1QmAmnoJRdq4K9btjkCM0%3D&amp;nvMid=5786210213&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">52<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=JeGjMt5iNuG8jC7uLI8UAP%2F%2F%2Fw%3D%3DsspKAMlS%2BJmrZgHmZ12q7RluqckbMgGvSnDoCWhYV7K01vZayOtQkNQKbsv%2B%2BueVZgVJsb%2B2kQ56ledC8O2l3CmIQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYb7yfk%2FxAhqEougrb5pDHjWcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykZRL9p0qB1AcJJbJrePKo3H5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpuA70mXv9Pgc16G2eb100HerIhSbytQHVFix20EMeN1DcCnIaWQZiGDpSIRmj9VowuyT71yi9V6bHpQ977omK2D6FURihOvVNK6%2BarovFEXYPQ431u6w0VnGxRIDS8%2FMJpR7UVCZp3ws1%2FNie8p11LdU6l34n%2BhExTwz7mP9tOnPtdEjB4ZJtcjuxf2dnsyEXT%2BDzDxwp7nT02YxkVA94lBzjTcXwoVM8lrhL6igy83LXeZDJLMvq4TQHBwah2gKPnLywBF6TPdyrHi5pSyQkVg1QmAmnoJRdq4K9btjkCM0%3D&amp;nvMid=5786210213&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">4개</em></a><span class="basicList_price__euNoD">9,880원
                            (100g당 1,235원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=JeGjMt5iNuG8jC7uLI8UAP%2F%2F%2Fw%3D%3DsspKAMlS%2BJmrZgHmZ12q7RluqckbMgGvSnDoCWhYV7K01vZayOtQkNQKbsv%2B%2BueVZgVJsb%2B2kQ56ledC8O2l3CmIQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYb7yfk%2FxAhqEougrb5pDHjWcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykZRL9p0qB1AcJJbJrePKo3H5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpuA70mXv9Pgc16G2eb100HerIhSbytQHVFix20EMeN1DcCnIaWQZiGDpSIRmj9VowuyT71yi9V6bHpQ977omK2D6FURihOvVNK6%2BarovFEXYPQ431u6w0VnGxRIDS8%2FMJpR7UVCZp3ws1%2FNie8p11LdU6l34n%2BhExTwz7mP9tOnPtdEjB4ZJtcjuxf2dnsyEXT%2BDzDxwp7nT02YxkVA94lBzjTcXwoVM8lrhL6igy83LXeZDJLMvq4TQHBwah2gKPnLywBF6TPdyrHi5pSyQkVg1QmAmnoJRdq4K9btjkCM0%3D&amp;nvMid=5786210213&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">32<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=J%2BOZbaEi9kMl8TF2cvFsQf%2F%2F%2Fw%3D%3DsENYgMT6J%2FW14%2FaaOHWKuUcuOlELMxoP6CndKThHZrp%2FD0AWU%2FasSPLGnk44ZiSgXlewXTHfL5e3ZOlfL6ri%2FWlih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G8kR2qiTwxn15XNEV6Vnkxhm1SuVApM1ivHjmEKy4cRSve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs5mhSs78HNUlEIa3HLj7F7n6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqFpYjbrHiiky5ipgMeWIgBT1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCoa9M66M0uUv9q8IQkdCjRqAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4xQWWJaYpXAP4ZGjGZViE%2FGov7tAU1fWckO6MZvpKmzrsYS74fNDjve9MbBz4TnvpnUpTzmQTeleeE0y%2Brv8xbHOTfGZF38nrH7KTZrXyIwBjrJZ%2BWc3awGxP156SzuWiVoWd0jB03C5aYq3HUc1IKtSSLJQZncWk8e8Ttfjz6Fs%3D&amp;nvMid=5786210213&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">5개</em></a><span class="basicList_price__euNoD">12,340원
                            (100g당 1,234원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=J%2BOZbaEi9kMl8TF2cvFsQf%2F%2F%2Fw%3D%3DsENYgMT6J%2FW14%2FaaOHWKuUcuOlELMxoP6CndKThHZrp%2FD0AWU%2FasSPLGnk44ZiSgXlewXTHfL5e3ZOlfL6ri%2FWlih2O4lnfTu2U4BQDAsrhSGCQS8Un2q3cpfkT6prtEOIeiwR157d%2FPVX5sOYll0YlEoogQ4kNr8sKolHBzKgfxMwMzf4u%2FXgVLeU7aK48EMw6ZjbtkbN7RD61dGUzg7G8kR2qiTwxn15XNEV6Vnkxhm1SuVApM1ivHjmEKy4cRSve%2FAPSpEBx%2Fq7qpnUHXIEtYiDwV4J8UsC0EptsvtFs5mhSs78HNUlEIa3HLj7F7n6B67eL%2FFaXNLZQi9Qyhfv8OmY27ZGze0Q%2BtXRlM4OxtarJoVrbEtunAYIkKGowOqFpYjbrHiiky5ipgMeWIgBT1nRJ4yoQ1ByXgZXYF4asUe2bDhC5C5s71xxKf5%2BXhCoa9M66M0uUv9q8IQkdCjRqAhfbmRc6T9Q91MqoVII6osqEREFnWu7tkx7k6TKRg4xQWWJaYpXAP4ZGjGZViE%2FGov7tAU1fWckO6MZvpKmzrsYS74fNDjve9MbBz4TnvpnUpTzmQTeleeE0y%2Brv8xbHOTfGZF38nrH7KTZrXyIwBjrJZ%2BWc3awGxP156SzuWiVoWd0jB03C5aYq3HUc1IKtSSLJQZncWk8e8Ttfjz6Fs%3D&amp;nvMid=5786210213&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">49<!-- -->개</span></a></li>
                    <li class="basicList_option__iDFgy"><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conprice"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=%2BWbb%2Fr1a2yUKBuDj2Hgsq%2F%2F%2F%2Fw%3D%3DsmJqXcMVl%2FdQyYjOMcYKYBluqckbMgGvSnDoCWhYV7K01vZayOtQkNQKbsv%2B%2BueVZspqJJgdxHZDdV0SyyQgBAGIQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYb7yfk%2FxAhqEougrb5pDHjWcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykauOjR4mIJazOXIFaauUKD%2F5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpTqFnYfoOJNlkVH3bKA8FuZlVwRe1rrtuvOE9PulSFxPcCnIaWQZiGDpSIRmj9VowuyT71yi9V6bHpQ977omK2D6FURihOvVNK6%2BarovFEXYPQ431u6w0VnGxRIDS8%2FMJpR7UVCZp3ws1%2FNie8p11LdU6l34n%2BhExTwz7mP9tOnPtdEjB4ZJtcjuxf2dnsyEXT%2BDzDxwp7nT02YxkVA94lBzjTcXwoVM8lrhL6igy83LXeZDJLMvq4TQHBwah2gKPnLywBF6TPdyrHi5pSyQkVg1QmAmnoJRdq4K9btjkCM0%3D&amp;nvMid=5786210213&amp;catId=50011943"><em
                                class="basicList_text__gCaiD">6개</em></a><span class="basicList_price__euNoD">14,670원
                            (100g당 1,222원)</span><a target="_blank" class="basicList_link__JLQJf" rel="noopener"
                            data-nclick="N=a:lst*C.conmall"
                            href="https://cr.shopping.naver.com/adcr.nhn?x=%2BWbb%2Fr1a2yUKBuDj2Hgsq%2F%2F%2F%2Fw%3D%3DsmJqXcMVl%2FdQyYjOMcYKYBluqckbMgGvSnDoCWhYV7K01vZayOtQkNQKbsv%2B%2BueVZspqJJgdxHZDdV0SyyQgBAGIQVJtgbggHcWqc%2FqTPrqqMM7CovxfMWu7V7Sbsr3eI%2B0ZLLDEmaANZoXIouYYApHbIA3j9r4y4hSJMixlwu0T5chZU5dmSRDV73GcP1pFAQ%2BD%2Fo9glb0ukJK6bM8miKIj1pnJbiGEKCZyuxCFYZYb7yfk%2FxAhqEougrb5pDHjWcShbrR9PNV7F8V4AmZIf7mrpJcZV%2F%2F2DaCP0JAJ5ykauOjR4mIJazOXIFaauUKD%2F5gwOprPNNUOX90vwBY%2BmeEPg%2F6PYJW9LpCSumzPJoigK7CtQzZWLlur1%2FFge4%2BEpTqFnYfoOJNlkVH3bKA8FuZlVwRe1rrtuvOE9PulSFxPcCnIaWQZiGDpSIRmj9VowuyT71yi9V6bHpQ977omK2D6FURihOvVNK6%2BarovFEXYPQ431u6w0VnGxRIDS8%2FMJpR7UVCZp3ws1%2FNie8p11LdU6l34n%2BhExTwz7mP9tOnPtdEjB4ZJtcjuxf2dnsyEXT%2BDzDxwp7nT02YxkVA94lBzjTcXwoVM8lrhL6igy83LXeZDJLMvq4TQHBwah2gKPnLywBF6TPdyrHi5pSyQkVg1QmAmnoJRdq4K9btjkCM0%3D&amp;nvMid=5786210213&amp;catId=50011943"><span
                                class="basicList_link_low__LvXKg">97<!-- -->개</span></a></li>
                </ul><a target="_blank" class="basicList_link_more_option__73RUB" rel="noopener"
                    data-nclick="N=a:lst*C.conmore"
                    href="https://cr.shopping.naver.com/adcr.nhn?x=9nQtbUgzncKzEgmQ1ktKGv%2F%2F%2Fw%3D%3DsxD%2B0AG4Z2iARIPF4erb1znQ0seun%2F33zy6Sqmv2nbfRNMRu08tuPY8jiMzqY%2FosArc%2FI73sobO4CY0TA3OBY5%2FK5o%2BRZGDibGWabTPYDtA9T5JDDNhynOBZEiIQFfYx030%2BAGAkSXtSmNrH2cOFPqusyPdtj2%2B7y0Uoslru8TzwXvcHdAkh2w2B%2BGiqrLfePgGwmPNX%2Fe%2BXkuZ30duRQYhldh3QIFKLZcos%2F2kaiXEOWa2jBqXEqAscb1z9en1rLqqVi8UZf2pAJMXEkGpNLUVQUvAwuFq4F8j4ObLxf4GroHrt4v8Vpc0tlCL1DKF%2B%2Fw6ZjbtkbN7RD61dGUzg7G1qsmhWtsS26cBgiQoajA6o3x%2FtWQ28DlabvkjFGU4UYISFv7n5uAItYPm5%2BaPBVoI6RHsB00DVDP4V3cNLCdWbjVbe78Qlgnk9vbCXlbcufsckzTqbxeSSgAFLHEsUV6SYmAVd24REXnT4zgpMp4R3Q4zTf3A5I7O98bPKr4J0RrQV4qbCUxaXGTCr5hzXrA8ipiDDtMY66xFyPZHConykNauEcRynSn%2F8orOK7nc90V%2B5zXN72u75PP5FiRZ%2BVzcbFSbCzY1R6m8%2FEsPgg%2B8JXc50eBITwugSNPH3Ok09sVpGw61BSdoQRvEGgfFlc5w%3D%3D&amp;nvMid=5786210213&amp;catId=50011943">옵션
                    더보기</a>
            </div>
        </li>
    </div>
</div>
'''

if __name__ == "__main__":
    app.run()



    
    