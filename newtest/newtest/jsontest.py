#-*- coding: utf-8 -*-
import json
from django.http import HttpResponse

def index(request):
    response_data = {
	"act": "articleFeed",
	"decrypt": "0",
	"rspdata": {
		"isEnd": 1,
		"segmenter":["s400","俄罗斯","报道","school"],
		"list": [
		{
			"content": {
				"categoryId": 12,
				"commentCount": 0,
				"contentUrl": "http://newsimg.onemt.co/test/article/content/906686192529984",
				"copyright": "",
				"featuredTime": 1510219366616,
				"id": 906686192529984,
				"imageCount": 1,
				"images": [
					{
						"alt": "",
						"height": 420,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/750x420_906686192529984_0.png",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/750x420_906686192529984_0.webp",
						"width": 750
					}
				],
				"isBn": 0,
				"isFavorite": None,
				"isLiked": None,
				"media": {
					"icon": "http://rs.newsapi.co/media/image/143880e1-bc61-43cf-8e0e-a313d4826c5c.png",
					"id": 33,
					"isFollowed": 0,
					"name": "عاجل"
				},
				"publishTime": 1510173286000,
				"regionId": 1,
				"shareUrl": "http://wwwdebug.hasrdaily.com/a/906686192529984?c=hasrdaily",
				"sourceUrl": "http://www.ajel.sa/local/1983261",
				"subcategoryId": -1,
				"thumbs": [
					{
						"alt": "",
						"height": 236,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/352x236_906686192529984_0.png",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/352x236_906686192529984_0.webp",
						"width": 352
					}
				],
				"title": "据媒体报道，土耳其和俄罗斯的S400防空导弹合同可能无法执行了，school lunch",
				"type": "text",
				"videoId": "",
				"videoSource": "",
				"videoTime": 0
			},
			"contentSet": "random",
			"isSticky": 0,
			"type": "article",
			"viewType": "instantView"
		},
		{
			"content": {
				"categoryId": 12,
				"commentCount": 0,
				"contentUrl": "http://newsimg.onemt.co/test/article/content/906759366398528",
				"copyright": "",
				"featuredTime": 1510219360086,
				"id": 906759366398528,
				"imageCount": 11,
				"images": [
					{
						"alt": "",
						"height": 420,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/750x420_906759366398528_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/750x420_906759366398528_0.webp",
						"width": 750
					},
					{
						"alt": "",
						"height": 420,
						"orderNo": 1,
						"tag": "<!--IMAGE#1-->",
						"url": "http://newsimg.onemt.co/test/article/image/750x420_906759366398528_1.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/750x420_906759366398528_1.webp",
						"width": 750
					},
					{
						"alt": "",
						"height": 420,
						"orderNo": 2,
						"tag": "<!--IMAGE#2-->",
						"url": "http://newsimg.onemt.co/test/article/image/750x420_906759366398528_2.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/750x420_906759366398528_2.webp",
						"width": 750
					}
				],
				"isBn": 0,
				"isFavorite": None,
				"isLiked": None,
				"media": {
					"icon": "http://rs.newsapi.co/media/image/eeac5529-899a-4f19-bb40-9cac25853884.png",
					"id": 17,
					"isFollowed": 1,
					"name": "سبق"
				},
				"publishTime": 1510171920000,
				"regionId": 1,
				"shareUrl": "http://wwwdebug.hasrdaily.com/a/906759366398528?c=hasrdaily",
				"sourceUrl": "https://sabq.org/SBm2nK",
				"subcategoryId": 99999,
				"thumbs": [
					{
						"alt": "",
						"height": 236,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/352x236_906759366398528_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/352x236_906759366398528_0.webp",
						"width": 352
					},
					{
						"alt": "",
						"height": 236,
						"orderNo": 1,
						"tag": "<!--IMAGE#1-->",
						"url": "http://newsimg.onemt.co/test/article/image/352x236_906759366398528_1.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/352x236_906759366398528_1.webp",
						"width": 352
					},
					{
						"alt": "",
						"height": 236,
						"orderNo": 2,
						"tag": "<!--IMAGE#2-->",
						"url": "http://newsimg.onemt.co/test/article/image/352x236_906759366398528_2.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/352x236_906759366398528_2.webp",
						"width": 352
					}
				],
				"title": "\"فيسيو\" تجهز الأخضر لمواجهة البرتغال.. والفريدي يلتحق بالبعثة",
				"type": "text",
				"videoId": "",
				"videoSource": "",
				"videoTime": 0
			},
			"contentSet": "random",
			"isSticky": 0,
			"type": "article",
			"viewType": "instantView"
		},
		{
			"content": {
				"categoryId": 12,
				"commentCount": 0,
				"contentUrl": "http://newsimg.onemt.co/test/article/content/906448795116096",
				"copyright": "",
				"featuredTime": 1510219353556,
				"id": 906448795116096,
				"imageCount": 0,
				"images": [
				],
				"isBn": 0,
				"isFavorite": None,
				"isLiked": None,
				"media": {
					"icon": "http://rs.newsapi.co/media/image/9ac15b7d-ef01-474e-ba69-562321c5272f.png",
					"id": 19,
					"isFollowed": 0,
					"name": "وكالة الأنباء السعودية"
				},
				"publishTime": 1510099200000,
				"regionId": 1,
				"shareUrl": "http://wwwdebug.hasrdaily.com/a/906448795116096?c=hasrdaily",
				"sourceUrl": "http://www.spa.gov.sa/viewstory.php?lang=ar&newsid=1685508",
				"subcategoryId": 99999,
				"thumbs": [
				],
				"title": "رياضي / رئيس الاتحاد السعودي لكرة القدم يؤكد ثقته بلاعبي منتخب الشباب لكسب بطاقة التأهل لنهائيات كأس آسيا",
				"type": "text",
				"videoId": "",
				"videoSource": "",
				"videoTime": 0
			},
			"contentSet": "random",
			"isSticky": 0,
			"type": "article",
			"viewType": "instantView"
		},
		{
			"content": {
				"categoryId": 12,
				"commentCount": 0,
				"contentUrl": "http://newsimg.onemt.co/test/article/content/906685603017280",
				"copyright": "",
				"featuredTime": 1510219347026,
				"id": 906685603017280,
				"imageCount": 1,
				"images": [
					{
						"alt": "",
						"height": 420,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/750x420_906685603017280_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/750x420_906685603017280_0.webp",
						"width": 750
					}
				],
				"isBn": 0,
				"isFavorite": None,
				"isLiked": None,
				"media": {
					"icon": "http://rs.newsapi.co/media/image/23b47e23-1498-4dbf-b814-e26b9337faeb.png",
					"id": 218,
					"isFollowed": 0,
					"name": "إرم"
				},
				"publishTime": 1510166124000,
				"regionId": 2,
				"shareUrl": "http://wwwdebug.hasrdaily.com/a/906685603017280?c=hasrdaily",
				"sourceUrl": "https://www.eremnews.com/sports/football/arab/egypt-sport/1060575",
				"subcategoryId": 12999,
				"thumbs": [
					{
						"alt": "",
						"height": 236,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/352x236_906685603017280_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/352x236_906685603017280_0.webp",
						"width": 352
					}
				],
				"title": "المصري البورسعيدي يضرب موعدًا مع وادي دجلة في دور 16 لكأس مصر",
				"type": "text",
				"videoId": "",
				"videoSource": "",
				"videoTime": 0
			},
			"contentSet": "random",
			"isSticky": 0,
			"type": "article",
			"viewType": "instantView"
		},
		{
			"content": {
				"categoryId": 12,
				"commentCount": 0,
				"contentUrl": "http://newsimg.onemt.co/test/article/content/906686408536640",
				"copyright": "",
				"featuredTime": 1510219340496,
				"id": 906686408536640,
				"imageCount": 1,
				"images": [
					{
						"alt": "",
						"height": 420,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/750x420_906686408536640_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/750x420_906686408536640_0.webp",
						"width": 750
					}
				],
				"isBn": 0,
				"isFavorite": None,
				"isLiked": None,
				"media": {
					"icon": "http://rs.newsapi.co/media/image/39eaf4fe-687a-428e-93c5-c0c3234d93af.png",
					"id": 20,
					"isFollowed": 0,
					"name": "البيان"
				},
				"publishTime": 1510170360000,
				"regionId": 2,
				"shareUrl": "http://wwwdebug.hasrdaily.com/a/906686408536640?c=hasrdaily",
				"sourceUrl": "http://www.albayan.ae/sports/emirates/2017-11-08-1.3093913",
				"subcategoryId": 12023,
				"thumbs": [
					{
						"alt": "",
						"height": 236,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/352x236_906686408536640_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/352x236_906686408536640_0.webp",
						"width": 352
					}
				],
				"title": "الفيفا يلزم كروزيرو البرازيلي بسداد 850 ألف دولار للوحدة",
				"type": "text",
				"videoId": "",
				"videoSource": "",
				"videoTime": 0
			},
			"contentSet": "random",
			"isSticky": 0,
			"type": "article",
			"viewType": "instantView"
		},
		{
			"content": {
				"categoryId": 12,
				"commentCount": 0,
				"contentUrl": "http://newsimg.onemt.co/test/article/content/906453905928768",
				"copyright": "",
				"featuredTime": 1510219333966,
				"id": 906453905928768,
				"imageCount": 1,
				"images": [
					{
						"alt": "",
						"height": 420,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/750x420_906453905928768_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/750x420_906453905928768_0.webp",
						"width": 750
					}
				],
				"isBn": 0,
				"isFavorite": None,
				"isLiked": None,
				"media": {
					"icon": "http://rs.newsapi.co/media/image/90facae3-9c93-4c70-94d2-744876190b95.png",
					"id": 92,
					"isFollowed": 0,
					"name": "ماب نيوز"
				},
				"publishTime": 1510137197000,
				"regionId": 1,
				"shareUrl": "http://wwwdebug.hasrdaily.com/a/906453905928768?c=hasrdaily",
				"sourceUrl": "http://mapkora.com/2039912/%d8%a8%d9%8a%d8%a8%d9%8a-%d9%8a%d8%ba%d8%b6%d8%a8-%d8%ac%d9%85%d8%a7%d9%87%d9%8a%d8%b1-%d8%b1%d9%8a%d8%a7%d9%84-%d9%85%d8%af%d8%b1%d9%8a%d8%af-%d8%a8%d9%87%d8%b0%d8%a7-%d8%a7%d9%84%d8%aa%d8%b5%d8%b1/",
				"subcategoryId": 12023,
				"thumbs": [
					{
						"alt": "",
						"height": 236,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/352x236_906453905928768_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/352x236_906453905928768_0.webp",
						"width": 352
					}
				],
				"title": "بيبي يغضب جماهير ريال مدريد بهذا التصريح",
				"type": "text",
				"videoId": "",
				"videoSource": "",
				"videoTime": 0
			},
			"contentSet": "random",
			"isSticky": 0,
			"type": "article",
			"viewType": "instantView"
		},
		{
			"content": {
				"categoryId": 12,
				"commentCount": 0,
				"contentUrl": "http://newsimg.onemt.co/test/article/content/906687629005376",
				"copyright": "",
				"featuredTime": 1510219327436,
				"id": 906687629005376,
				"imageCount": 1,
				"images": [
					{
						"alt": "",
						"height": 420,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/750x420_906687629005376_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/750x420_906687629005376_0.webp",
						"width": 750
					}
				],
				"isBn": 0,
				"isFavorite": None,
				"isLiked": None,
				"media": {
					"icon": "http://rs.newsapi.co/media/image/4e040794-73ae-4c4b-83b2-758f51c28295.png",
					"id": 68,
					"isFollowed": 0,
					"name": "صدى"
				},
				"publishTime": 1510174239000,
				"regionId": 1,
				"shareUrl": "http://wwwdebug.hasrdaily.com/a/906687629005376?c=hasrdaily",
				"sourceUrl": "https://www.slaati.com/2017/11/08/p910426.html",
				"subcategoryId": 99999,
				"thumbs": [
					{
						"alt": "",
						"height": 236,
						"orderNo": 0,
						"tag": "<!--IMAGE#0-->",
						"url": "http://newsimg.onemt.co/test/article/image/352x236_906687629005376_0.jpg",
						"webpUrl": "http://newsimg.onemt.co/test/article/image/352x236_906687629005376_0.webp",
						"width": 352
					}
				],
				"title": "عادل الملحم : العديد من الأندية السعودية عليها قضايا كثيرة في الفيفا",
				"type": "text",
				"videoId": "",
				"videoSource": "",
				"videoTime": 0
			},
			"contentSet": "random",
			"isSticky": 0,
			"type": "article",
			"viewType": "instantView"
		}
	],
		"snapId": "123",
		"tips": "اخترنا لك  7 أخبار جديدة."
	},
	"rtncode": "SUCCESS",
	"rtnmsg": "操作成功"
}

    return HttpResponse(json.dumps(response_data),content_type="application/json")