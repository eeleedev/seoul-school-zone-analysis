# 2. 한글 폰트 설정
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl

font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
fm.fontManager.addfont(font_path)
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
mpl.rcParams['axes.unicode_minus'] = False

#. GeoDataFrame 불러오기
import geopandas as gpd

# 파일 경로 (예: content/폴더 하위에 저장했다고 가정)
shp_path = "/content/교육행정구역.shp"

# GeoDataFrame 로딩 + 좌표계 변환
gdf = gpd.read_file(shp_path)
gdf = gdf.to_crs("EPSG:4326")

#4. 서울특별시교육청만 필터링
seoul_gdf = gdf[gdf["EDU_UP_NM"] == "서울특별시교육청"].copy()

# 5. 시각화 (교육청 이름 표시 포함)

fig, ax = plt.subplots(figsize=(10, 10))
seoul_gdf.plot(ax=ax, edgecolor="black", color="skyblue")

# 레이블 위치 보정이 필요할 수 있음 → centroid 기반
for idx, row in seoul_gdf.iterrows():
    centroid = row.geometry.centroid
    ax.annotate(
        text=str(row["EDU_NM"]).strip(),
        xy=(centroid.x, centroid.y),
        fontsize=10,
        ha="center",
        color="black"
    )

plt.title("서울특별시 교육지원청 지도", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.show()