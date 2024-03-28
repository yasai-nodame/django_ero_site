from django.shortcuts import render
import os
from .forms import TitleForm 
from .models import Ero_title 


#indexメソッドの定義
def index(request):
    path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\imgapp\\images'
    
    files = []
    files_name = []
    files_index = []
    title_list = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    
    #拡張子のついたファイルを取得
    for i in os.listdir(path):
        files.append(i)
    
    #動画リンクにいくときのhtmlリンクを作成、追加
    # for index in range(len(files)):
    #     html_path = f'ero_{index}.html'
    #     files_index.append(html_path)
    title = Ero_title.objects.all()
    
    for i in range(len(files)):
        title_list.append(str(title[i]))
        
    
    file_zip = zip(files,files_name,title_list)
    return render(request,'ero_template/index.html',{'file_zip':file_zip,'title_form':f})


def search(request):
    #キーワード送信をPOSTメソッドで送信し、受け取ったtitle imgのtitleがデータベースに合致したら title imgを表示するページを作る
    name = request.POST['title']
    get_title = Ero_title.objects.all()
    
    str_name = str(name)
    str_get_title = ''
    
    for i in range(90):
        if str_name == str(get_title[i]):
            str_get_title = str(get_title[i])
        
    return render(request,'ero_template/search.html',{'name':str_name,'get_title':str_get_title})


def ero_0(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[0]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[0]
    
    return render(request,'ero_template/Gカップ８頭身グラマー美女が電車痴漢に遭遇し生マン膣挿入中出しどっくん.html',{'movie':movie,'file_name':file_name,'title_form':f})

def ero_1(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[1]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[1]
    
    return render(request,'ero_template/「いくっ!いくっ!!」電車痴漢で悶え声漏らし続けて限界突破する制服JK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_2(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[2]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[2]
    
    return render(request,'ero_template/「やだっ…やだっ…あっ」満員電車痴漢で美巨乳揉みしだかれる姿Hな美女子.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_3(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[3]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[3]
    
    return render(request,'ero_template/「痴漢させて」言われた女子が電車内で戸惑うもお触り翻弄され股間弄り絶頂.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_4(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[4]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[4]
    
    return render(request,'ero_template/いつも見るたび痴漢されてるという巨乳OLが電車ドア付近で痴漢されてる姿.html',{'movie':movie,'file_name':file_name,'title_form':f})



def ero_5(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[5]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[5]
    
    return render(request,'ero_template/されるがままな大人しめお姉さんが不安顔しながら電車痴漢されお漏らし噴射.html',{'movie':movie,'file_name':file_name,'title_form':f})



def ero_6(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[6]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[6]
    
    return render(request,'ero_template/しっかり者表情もちな童顔JKが電車痴漢で性感極まり喘ぐほどイクHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})



def ero_7(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[7]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[7]
    
    return render(request,'ero_template/アイドル顔な美系JKが電車内対面痴漢されクリトリス弄りにヒクッ感度反応.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_8(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[8]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[8]
    
    return render(request,'ero_template/コスプレしたら萌えそうな童顔女子が電車痴漢で下半身弄られ中出し精液垂れ.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_9(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[9]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[9]
    
    return render(request,'ero_template/ツルツルスベスベな桃尻を指で堪能され続けるJKの電車痴漢盗撮エロ動画.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_10(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[10]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[10]
    
    return render(request,'ero_template/ツルツル美尻そそるパイパン美人OLが満員電車痴漢され無言困惑表情ガマン.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_11(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[11]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[11]
    
    return render(request,'ero_template/ドア付近奥に追い込まれた囲み集団痴漢で性感的お触りされ続ける巨乳JK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_12(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[12]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[12]
    
    return render(request,'ero_template/ハ リある美尻そそるツン系JKが電車痴漢で肉棒擦り付けられ表情歪め.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_13(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[13]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[13]
    
    return render(request,'ero_template/パパ活モデル体型女子が電車痴漢され露骨に嫌がりながらイキまくるHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_14(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[14]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[14]
    
    return render(request,'ero_template/パパ活会い２度目の男から電車痴漢でザーメン膣垂れハメ汚される可愛い女子.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_15(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[15]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[15]
    
    return render(request,'ero_template/パンチラ狙う男が我慢できなくなるほど最高尻もちJKが電車痴漢される姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_16(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[16]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[16]
    
    return render(request,'ero_template/パンチラ盗 撮だけでは飽き足らない男から電車痴漢までされちゃうJKのHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_17(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[17]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[17]
    
    return render(request,'ero_template/パンツ食い込みノーパン疑惑級な女子大生が満員電車痴漢で強制性感ガマン.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_18(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[18]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[18]
    
    return render(request,'ero_template/ムチムチなハード型美尻にHなパンティーそそる女性客の電車痴漢弄ばれ姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_19(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[19]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[19]
    
    return render(request,'ero_template/ヨガ講師系セクシーボディそそる美女が電車痴漢され徹底膣責めグリグリ×２.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_20(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[20]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[20]
    
    return render(request,'ero_template/下校ラッシ ュ電車内で可愛いJKが痴漢遭遇し乳首チロチロ陰部弄り愛液噴出.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_21(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[21]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[21]
    
    return render(request,'ero_template/乳首に軽く触れられただけで身体締める美尻JKが電車痴漢され潮吹き漏らし.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_22(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[22]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[22]
    
    return render(request,'ero_template/以前電車痴 漢された性感忘れられず再電車痴漢され絶頂仕草みせるOLのHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_23(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[23]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[23]
    
    return render(request,'ero_template/先生と初体験２日前に済ませた巨乳JKが電車痴漢とハメ撮りで精液膣注がれ.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_24(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[24]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[24]
    
    return render(request,'ero_template/前回痴漢された男に再会しパンツ濡れたJKが電車痴漢で自ら男根擦り付け.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_25(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[25]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[25]
    
    return render(request,'ero_template/可愛いJKが電車痴漢で無言大量お漏らしイキ与えられ多目的トイレ膣中出し.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_26(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[26]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[26]
    
    return render(request,'ero_template/可愛い声で絶 叫しながら鬼畜電車痴漢で対面座位ハメ中出し決められる美女.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_27(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[27]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[27]
    
    return render(request,'ero_template/可愛い清純顔なFカップJKが電車痴漢で愛液ヌレヌレ絶頂繰り返すHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_28(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[28]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[28]
    
    return render(request,'ero_template/大人しめ性格に攻 撃的巨乳ギャップそそるJKが電車痴漢翻弄されるHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_29(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[29]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[29]
    
    return render(request,'ero_template/天然性格そうな可愛い癒し顔JKが電車痴漢とハメ撮りでイキ過ぎ舌出し悶絶.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_30(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[30]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[30]
    
    return render(request,'ero_template/女子校系JKが電車痴漢で困惑しながら性感込み上げイクイク連呼エンドレス.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_31(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[31]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[31]
    
    return render(request,'ero_template/媚薬効いた身体を電車痴漢で弄ばれ乳首・電マ・バイブで３連イキする美女.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_32(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[32]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[32]
    
    return render(request,'ero_template/媚薬盛られた電車痴漢 でビックンビクビク雌汁漏らし腰砕けイキする美女子.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_33(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[33]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[33]
    
    return render(request,'ero_template/存在してるだけで次々男寄ってきそうな美女子が電車痴漢され性感究極声我慢.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_34(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[34]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[34]
    
    return render(request,'ero_template/恥部触られると感度 反応すぐ示す可愛い女子が電車痴漢で限界恥汁漏らし絶頂.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_35(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[35]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[35]
    
    return render(request,'ero_template/敏感箇所を徹底責める痴漢掲示板主達から満員電車痴漢される女子のHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_36(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[36]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[36]
    
    return render(request,'ero_template/数年後の完全大人ボディ想像してしまう可愛いJKの電車痴漢汚され姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_37(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[37]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[37]
    
    return render(request,'ero_template/桃がパンツ穿いてるような尻肉そそるJKが電車痴漢されるドキドキ展開.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_38(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[38]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[38]
    
    return render(request,'ero_template/泣きべそや降りる連呼しても電 車痴漢止まらず強制中出しされちゃう美女.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_39(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[39]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[39]
    
    return render(request,'ero_template/涼しげポロシャツ似合う可愛いJKが電車痴漢に遭遇し愛液音立て過激指マン.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_40(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[40]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[40]
    
    return render(request,'ero_template/清純童顔な大人ボディOLが電車痴 漢で２度潮吹きからハメ撮り妊娠確定！？.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_41(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[41]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[41]
    
    return render(request,'ero_template/満員痴漢で抵抗せず成されるまま触られ続けビックビック感度反応示す女性客.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_42(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[42]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[42]
    
    return render(request,'ero_template/満員電車内で前後痴漢男達の舐 め系お触りにジッと無言耐える身長低めなJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_43(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[43]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[43]
    
    return render(request,'ero_template/満員電車密着痴漢で多彩な表情しながら望まない気持ち良さに無言耐えるJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_44(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[44]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[44]
    
    return render(request,'ero_template/満員電車痴漢され嫌さ感・強制 性感・羞恥感混ぜた表情そそる巨乳熟女OL.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_45(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[45]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[45]
    
    return render(request,'ero_template/満員電車痴漢で大胆に弄る痴漢男の股間弄りに耐え続ける姿そそる美尻女子.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_46(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[46]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[46]
    
    return render(request,'ero_template/無防備前かがみ姿眩しい可愛いJK が小ぶり美尻揉み痴漢され中出しドックン.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_47(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[47]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[47]
    
    return render(request,'ero_template/狭膣そそるプリ尻JKが電車痴漢に我慢続けるも直マンスジ触られ感度反応.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_48(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[48]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[48]
    
    return render(request,'ero_template/男勝り性格もちに見えるも電車痴漢 抵抗できず息乱し悶絶続けるスッピンJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_49(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[49]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[49]
    
    return render(request,'ero_template/男勝り的ボーイッシュ系な可愛いJKが電車痴漢に遭遇し本気粘着愛液濡れ.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_50(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[50]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[50]
    
    return render(request,'ero_template/痴漢に我慢する恍惚表情たまらないノ ーパンノーブラOLの電車痴漢され姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_51(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[51]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[51]
    
    return render(request,'ero_template/痴漢多発で有名な電車へ乗り込み痴漢され盗撮する企画に参加した巨乳女子.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_52(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[52]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[52]
    
    return render(request,'ero_template/痴漢多発電車内で乳首摘み伸ばし性感＆ 股間過激弄りされ悶絶する巨乳女子.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_53(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[53]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[53]
    
    return render(request,'ero_template/痴漢掲示板主達から満員電車内でエンドレス性感与えられ身悶え続ける女子.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_54(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[54]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[54]
    
    return render(request,'ero_template/目的地の駅に着くまで痴漢されても電車 降りないJKが下半身弄られ続ける姿.html',{'movie':movie,'file_name':file_name,'title_form':f})



def ero_55(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[55]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[55]
    
    return render(request,'ero_template/睡眠痴漢され気づき激怒帰宅した先の電車で集団痴漢されるマッサージ嬢.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_56(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[56]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[56]
    
    return render(request,'ero_template/突然の電車痴漢に「やめてください」言う も官能声発してイキまくるJK.html',{'movie':movie,'file_name':file_name,'title_form':f})

def ero_57(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[57]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[57]
    
    return render(request,'ero_template/童顔優等生系JKが電車痴漢され「やめて～んっん～あっいっくう～」エンドレス.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_58(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[58]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[58]
    
    return render(request,'ero_template/童顔大人スタイルそそる美女子が電車痴漢 に遭遇し吐息漏らして限界アクメ.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_59(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[59]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[59]
    
    return render(request,'ero_template/美爆乳フェロモンボディもちな百貨店勤務美女が電車痴漢で汚されるHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_60(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[60]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[60]
    
    return render(request,'ero_template/羞恥と困惑心境あるも強制性感電車痴漢でアへ顔するほどイカされまくる美女.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_61(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[61]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[61]
    
    return render(request,'ero_template/肉厚美尻と美パイパンそそる可愛い童顔JKが電車痴漢され指マンヌチャ×２.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_62(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[62]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[62]
    
    return render(request,'ero_template/自然と目で追いかけてしまいそうな清楚容姿美女の電車痴漢され盗撮的映像.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_63(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[63]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[63]
    
    return render(request,'ero_template/調教したくなる雰囲気MAXな癒し顔にIカップそそるJKの電車痴漢され姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_64(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[64]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[64]
    
    return render(request,'ero_template/遅刻時間帯の満員電車内で痴漢に遭遇し迷惑顔し ながら上下半身弄られるJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_65(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[65]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[65]
    
    return render(request,'ero_template/遊んでない感ある未処理的な剛陰毛そそるお姉さんが電車痴漢されるHな姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_66(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[66]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[66]
    
    return render(request,'ero_template/隣に住んでそうな主婦系爆乳熟女が電車痴漢に遭遇し性感我慢小刻みヒクヒク.html',{'movie':movie,'file_name':file_name,'title_form':f})

def ero_67(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[67]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[67]
    
    return render(request,'ero_template/電車内で密着痴漢され乗り換え先でも囲み痴漢で硬乳首＆股間弄られるＯL.html',{'movie':movie,'file_name':file_name,'title_form':f})

def ero_68(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[68]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[68]
    
    return render(request,'ero_template/電車内で痴漢交渉OKした乳首敏感なHカップ女子大 生の触られ乳首イキ姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_69(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[69]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[69]
    
    return render(request,'ero_template/電車内で自ら痴漢誘い何度も絶頂してはハメ行為中出し許可する可愛いJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_70(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[70]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[70]
    
    return render(request,'ero_template/電車内で角誘導囲み痴漢され股間弄られ続けて乳首勃起 お漏らしするお姉さん.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_71(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[71]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[71]
    
    return render(request,'ero_template/電車内で集団痴漢されお触りOKそうな表情しながら上下半身弄られイク淑女.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_72(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[72]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[72]
    
    return render(request,'ero_template/電車座席痴漢され強張った表情するもジッとしたまま オッパイ触られる女性客.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_73(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[73]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[73]
    
    return render(request,'ero_template/電車痴漢で「いくっイクッ」触られるほどパンツ染み広がる下半身そそるJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_74(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[74]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[74]
    
    return render(request,'ero_template/電車痴漢で徹底的下半身責めされ何度もイクイク連 呼絶頂しちゃう可愛いJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_75(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[75]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[75]
    
    return render(request,'ero_template/電車痴漢で痴漢男の股間触るほど性感与えられ極まるも無言我慢続けるOL.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_76(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[76]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[76]
    
    return render(request,'ero_template/電車痴漢に気づき迷惑がるも感じまくるJKが痴漢男ト イレ連れ込みハメ堪能.html',{'movie':movie,'file_name':file_name,'title_form':f})



def ero_77(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[77]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[77]
    
    return render(request,'ero_template/電車痴漢に遭遇し「だめっ」小声で言うのがそそるJKの感度良好絶頂MAX姿.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_78(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[78]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[78]
    
    return render(request,'ero_template/電車痴漢に遭遇し乳頭クリクリ股間激しく弄られ下半身震わせ恥汁漏らすOL.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_79(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[79]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[79]
    
    return render(request,'ero_template/電車痴漢に遭遇し嫌なのに性感帯刺激され徐々に込み上げてしまうJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_80(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[80]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[80]
    
    return render(request,'ero_template/電車痴漢に遭遇し露骨に嫌がるも愛液濡らして強制中出しされ る留学生女子.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_81(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[81]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[81]
    
    return render(request,'ero_template/電車相席で成長途中そうなオッパイ摘み痴漢される制服女子のHな一部始終.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_82(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[82]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[82]
    
    return render(request,'ero_template/電車走行音生々しい車内で震える痴漢男の手で様子伺い下半身痴漢されるJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_83(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[83]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[83]
    
    return render(request,'ero_template/電車集団痴漢でセクシーボディ堪能されヤダヤダ連呼中出し決められる美女.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_84(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[84]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[84]
    
    return render(request,'ero_template/静かな混雑列車内で乳房とマンスジ同時弄り痴漢されるJKを盗撮 的近写堪能.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_85(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[85]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[85]
    
    return render(request,'ero_template/静かな満員電車内で上下半身同時カオス痴漢され我慢続ける姿そそる柔乳JK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_86(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[86]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[86]
    
    return render(request,'ero_template/静かな満員電車内で前後密着痴漢され終始乳首チロチロ下半身弄 り耐えるJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_87(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[87]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[87]
    
    return render(request,'ero_template/静かな満員電車内で迷惑そうな表情しながら痴漢耐える天然HカップOL.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_88(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[88]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[88]
    
    return render(request,'ero_template/静かな電車内で強制痴漢性感に平静保ち続けながら限界潮吹きしちゃうJK.html',{'movie':movie,'file_name':file_name,'title_form':f})


def ero_89(request):
    movie_path = 'C:\\Users\\user\\ERO_APP\\ero_app_django\\ero_display_field\\static\\movie_folda'
    
    movie_link = []
    files_name = []
    
    f = TitleForm()
    
    #ファイル名取得
    for i in os.listdir(movie_path):
        file = os.path.basename(i)
        files_name.append(os.path.splitext(file)[0])
    file_name = files_name[89]
    
    #動画リンクを取得
    for link in os.listdir(movie_path):
        movie_link.append(link)
    movie = movie_link[89]
    
    return render(request,'ero_template/顔立ちエッチな美巨乳JKが集団電車痴漢に遭遇し「もうだめえ～」永遠悶え.html',{'movie':movie,'file_name':file_name,'title_form':f})



