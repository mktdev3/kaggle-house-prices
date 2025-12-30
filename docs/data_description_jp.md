# データセット詳細 (Data Description)

Kaggle House Pricesデータセットの81個の特徴量（カラム）に関する日本語の解説まとめです。

## 1. 土地・立地 (Land & Location)
土地の広さ、形状、場所など、不動産価値の基礎となる情報です。

| カラム名 | 説明 | 備考 |
| :--- | :--- | :--- |
| **MSSubClass** | 建物のクラス | 2階建て、1946年以降建築など、建物のタイプを示すコード。 |
| **MSZoning** | ゾーニング区分 | RL（低密度住宅地）、RM（中密度住宅地）、C（商業地）など。 |
| **LotFrontage** | 間口の距離 | 接している道路の長さ（フィート）。 |
| **LotArea** | 敷地面積 | 土地の広さ（平方フィート）。 |
| **Street** | 接面道路の種類 | Pave（舗装）、Grvl（砂利）。 |
| **Alley** | 路地へのアクセス | Pave（舗装）、Grvl（砂利）、NA（なし）。 |
| **LotShape** | 土地の形状 | Reg（正方形に近い）、IR1（不規則）など。 |
| **LandContour** | 土地の平坦さ | Lvl（平坦）、Bnk（傾斜あり）など。 |
| **Utilities** | インフラ設備 | 電気、ガス、水道の有無。 |
| **LotConfig** | 区画の配置 | Corner（角地）、CulDSac（袋小路）など。 |
| **LandSlope** | 土地の傾斜 | Gtl（緩やか）、Mod（適度）、Sev（急）。 |
| **Neighborhood** | 地区名 | Ames市内の地区。**価格への影響が大きい重要特徴量**。 |
| **Condition1/2** | 近接条件 | 幹線道路や鉄道に近いか、公園に近いかなど。 |

## 2. 建物構造・外装 (Building & Exterior)
建物の種類、スタイル、外壁の材質など。

| カラム名 | 説明 | 備考 |
| :--- | :--- | :--- |
| **BldgType** | 住居タイプ | 1Fam（一戸建て）、TwnhsE（タウンハウス端）など。 |
| **HouseStyle** | 建築スタイル | 1Story（平屋）、2Story（2階建て）など。 |
| **OverallQual** | **全体品質** | 建物の全体的な材質と仕上がりを1〜10で評価。**最重要**。 |
| **OverallCond** | **全体状態** | 建物の全体的な状態を1〜10で評価。 |
| **YearBuilt** | 建築年 | 新しいほど高い傾向があるが、古い家でもリノベ済みなら高い。 |
| **YearRemodAdd** | リフォーム年 | リフォームしていない場合は建築年と同じ。 |
| **RoofStyle** | 屋根のタイプ | Gable（切妻）、Hip（寄棟）など。 |
| **RoofMatl** | 屋根の材質 | shingle（こけら板）など。 |
| **Exterior1st/2nd** | 外壁材 | VinylSd（ビニールサイディング）、MetalSd（金属）など。 |
| **MasVnrType** | 化粧積み(石・レンガ) | 外壁の装飾部分のタイプ。 |
| **MasVnrArea** | 化粧積みの面積 | 装飾部分の面積。 |
| **ExterQual** | 外装の品質 | Ex（Excellent）〜Po（Poor）。 |
| **ExterCond** | 外装の状態 | Ex（Excellent）〜Po（Poor）。 |
| **Foundation** | 基礎の種類 | PConc（コンクリート）、CBlock（ブロック）、BrkTil（レンガ＆タイル）。 |

## 3. 内装・設備 (Interior & Utilities)
居住空間の広さ、部屋数、設備の質など。

| カラム名 | 説明 | 備考 |
| :--- | :--- | :--- |
| **BsmtQual** | 地下室の高さ | 地下室の天井の高さによる評価。 |
| **BsmtCond** | 地下室の状態 | 一般的な状態。 |
| **BsmtExposure** | 地下室の露出 | ウォークアウト（庭に出られる）などの露出度。 |
| **BsmtFinType1/2** | 地下仕上がり | GLQ（Good Living Quarters）などの仕上がりランク。 |
| **BsmtFinSF1/2** | 地下仕上り面積 | 仕上がっている部分の面積。 |
| **BsmtUnfSF** | 地下未仕上り面積 | 仕上がっていない部分の面積。 |
| **TotalBsmtSF** | **地下室総面積** | 地下全体の広さ。**広さは価格に直結する**。 |
| **Heating** | 暖房の種類 | GasA（ガス）などが一般的。 |
| **HeatingQC** | 暖房の品質 | Ex〜Po。 |
| **CentralAir** | セントラルエアコン | Y（あり）/ N（なし）。現代の家ではYが標準。 |
| **Electrical** | 電気設備 | ブレーカーやヒューズの種類。 |
| **1stFlrSF** | **1階床面積** | 1階の広さ。 |
| **2ndFlrSF** | 2階床面積 | 2階の広さ。 |
| **LowQualFinSF** | 低品質仕上り面積 | 全フロアの低品質な仕上がり部分の面積。 |
| **GrLivArea** | **地上居住面積** | 地上（地下を除く）にある居住スペースの総面積。**非常に重要**。 |
| **BsmtFull/HalfBath**| 地下バスルーム | 地下にあるフル/ハーフバスルームの数。 |
| **Full/HalfBath** | 地上のバスルーム | 地上にあるフル/ハーフバスルームの数。 |
| **BedroomAbvGr** | 寝室数 | 地上の寝室の数。 |
| **KitchenAbvGr** | キッチン数 | 地上のキッチンの数。 |
| **KitchenQual** | キッチン品質 | Ex〜Po。**重要**。 |
| **TotRmsAbvGrd** | 総部屋数 | バスルームを除く地上の部屋数。 |
| **Functional** | 機能性 | Typ（典型的）〜Sal（損傷あり）。通常はTyp。 |
| **Fireplaces** | 暖炉の数 | 暖炉の数。 |
| **FireplaceQu** | 暖炉の品質 | 暖炉がある場合の品質。 |

## 4. ガレージ・外構 (Garage & Outdoor)
車庫や庭の設備について。

| カラム名 | 説明 | 備考 |
| :--- | :--- | :--- |
| **GarageType** | ガレージタイプ | BuiltIn（組み込み）、Attchd（接続）、Detchd（独立）。 |
| **GarageYrBlt** | ガレージ建築年 | ガレージが建てられた年。 |
| **GarageFinish** | ガレージ内装 | Fin（完了）、RFn（粗仕上げ）、Unf（未完了）。 |
| **GarageCars** | **車庫収容台数** | 車が何台入るか。**重要**。 |
| **GarageArea** | 車庫面積 | ガレージの広さ。 |
| **GarageQual** | ガレージ品質 | Ex〜Po。 |
| **GarageCond** | ガレージ状態 | Ex〜Po。 |
| **PavedDrive** | 私道の舗装 | Y（舗装）、P（部分的）、N（砂利/土）。 |
| **WoodDeckSF** | ウッドデッキ面積 | 木製デッキの広さ。 |
| **OpenPorchSF** | オープンポーチ面積 | 屋根付きだが壁のないポーチの広さ。 |
| **EnclosedPorch** | 囲いポーチ面積 | 壁で囲まれたポーチの広さ。 |
| **3SsnPorch** | 3シーズンポーチ | 春夏秋用ポーチの広さ。 |
| **ScreenPorch** | 網戸ポーチ | 網戸付きポーチの広さ。 |
| **PoolArea** | プール面積 | プールの広さ。 |
| **PoolQC** | プール品質 | プールの質。ほとんどの家にはプールがない（NA）。 |
| **Fence** | フェンス | プライバシーや木の質など。 |
| **MiscFeature** | その他設備 | エレベーター、テニスコートなど。 |
| **MiscVal** | その他設備の価値 | 金額換算した価値。 |

## 5. 売却情報 (Sale Information)
売買契約に関する情報。

| カラム名 | 説明 | 備考 |
| :--- | :--- | :--- |
| **MoSold** |売却月 | 何月に売れたか。 |
| **YrSold** | 売却年 | 何年に売れたか（2006-2010）。 |
| **SaleType** | 販売タイプ | WD（通常）、New（新築）など。 |
| **SaleCondition** | 販売条件 | Normal（通常）、Abnorml（異常）、Partial（未完成/新築）など。 |
| **SalePrice** | **販売価格** | **目的変数（Target）**。これを予測します。 |
