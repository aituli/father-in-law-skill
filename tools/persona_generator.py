#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Persona Generator - 根据老丈人类型自动生成 Persona

根据指定的老丈人类型，自动生成对应的六层 Persona 结构。
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Dict, List, Optional


# 十种老丈人类型定义
FATHER_IN_LAW_TYPES = {
    "traditional": {
        "name": "传统威严型",
        "name_en": "Traditional Authoritative",
        "traits": ["家长权威", "不善表达", "重面子", "威严"],
        "description": "话不多但很有分量，让你有点怕"
    },
    "humorous": {
        "name": "幽默风趣型",
        "name_en": "Humorous & Easygoing",
        "traits": ["爱开玩笑", "自来熟", "没架子", "随和"],
        "description": "第一次见面就能聊，爱调侃"
    },
    "silent": {
        "name": "沉默寡言型",
        "name_en": "Silent & Reserved",
        "traits": ["话少", "内敛", "观察型", "稳重"],
        "description": "饭桌上听得多说得少，难猜心思"
    },
    "drinking": {
        "name": "酒桌话痨型",
        "name_en": "Talkative When Drunk",
        "traits": ["酒后吐真言", "情感外露", "豪爽"],
        "description": "平时话少，三杯下肚变话痨"
    },
    "intellectual": {
        "name": "知识分子型",
        "name_en": "Intellectual",
        "traits": ["高学历", "理性", "爱讲道理", "有文化"],
        "description": "聊天偏文化历史，喜欢教育"
    },
    "business": {
        "name": "经商精明型",
        "name_en": "Business-Savvy",
        "traits": ["精明", "务实", "利益导向", "会算计"],
        "description": "喜欢谈赚钱、试探你的条件"
    },
    "retired_official": {
        "name": "退休干部型",
        "name_en": "Retired Official",
        "traits": ["官架子", "讲规矩", "爱说教", "关心时事"],
        "description": "说话有领导腔，关心国家大事"
    },
    "rural": {
        "name": "农村朴实型",
        "name_en": "Rural & Simple",
        "traits": ["朴实", "勤劳", "不善言辞", "实在"],
        "description": "默默付出，不看重物质条件"
    },
    "critical": {
        "name": "挑剔苛刻型",
        "name_en": "Critical & Demanding",
        "traits": ["完美主义", "难取悦", "比较型", "苛刻"],
        "description": "总有不满意，拿你和别人比"
    },
    "modern": {
        "name": "开明现代型",
        "name_en": "Modern & Open-minded",
        "traits": ["思想开放", "尊重隐私", "平等", "理解"],
        "description": "像朋友一样相处，不干涉"
    }
}


def generate_layer_0(fil_type: str) -> str:
    """生成 Layer 0: 硬覆盖层"""
    layer_0_templates = {
        "traditional": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 对女儿有强烈的保护欲和控制欲
- 在任何场合都要维护家长权威
- 从不直接表达关爱，但会通过行动体现
- 对女婿的考察期长，不容易完全信任""",
        
        "humorous": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 用幽默化解尴尬，不喜欢严肃的氛围
- 自来熟，容易和人打成一片
- 对女婿像朋友一样，但尊重边界
- 喜欢活跃气氛，是聚会的中心""",
        
        "silent": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 话少但每句话都有分量
- 善于观察，不轻易下判断
- 对女婿的态度藏在细节中
- 不喜欢被逼迫表达""",
        
        "drinking": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 酒是沟通的媒介，不喝酒难以交心
- 酒后会说出平时不敢说的话
- 酒桌上最能看出真情实意
- 对能喝酒的女婿更有好感""",
        
        "intellectual": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 重视教育和知识，喜欢讲道理
- 对女婿的学历和工作有一定期望
- 喜欢用历史和文化来教育人
- 理性思考，不轻易被情绪左右""",
        
        "business": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 务实，看重实际利益和能力
- 对女婿的经济实力和前途很关注
- 精于算计，但不会明显表现出来
- 认为经济基础决定家庭地位""",
        
        "retired_official": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 重视规矩和等级秩序
- 说话有官腔，喜欢说教
- 关心时事政治，喜欢讨论国家大事
- 对女婿的社会地位和人脉有要求""",
        
        "rural": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 朴实勤劳，相信双手创造价值
- 不善言辞，但行动力强
- 不看重物质条件，看重人品
- 对女婿的要求不高，只要能对女儿好""",
        
        "critical": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 完美主义，对任何事情都有高标准
- 容易发现别人的缺点，难以取悦
- 喜欢拿女婿和别人比较
- 对女儿的婚事有很高的期望""",
        
        "modern": """## Layer 0: 硬覆盖层（核心性格规则）

### 不可违背的规则
- 尊重子女的选择，不干涉私事
- 与女婿平等相处，像朋友一样
- 思想开放，能接受新事物
- 相信女儿的眼光，不多加评判"""
    }
    return layer_0_templates.get(fil_type, layer_0_templates["traditional"])


def generate_layer_1(fil_type: str, name: str = "老丈人", age: int = 65) -> str:
    """生成 Layer 1: 身份层"""
    occupations = {
        "traditional": "退休工程师/教师",
        "humorous": "退休体育老师/销售员",
        "silent": "退休技工/会计",
        "drinking": "退休工人/个体户",
        "intellectual": "退休教授/研究员",
        "business": "退休商人/企业主",
        "retired_official": "退休公务员/领导干部",
        "rural": "农民/退休农民工",
        "critical": "退休医生/工程师",
        "modern": "退休IT/自由职业"
    }
    
    locations = {
        "traditional": "城市，与女儿同住或就近",
        "humorous": "城市，周末聚会",
        "silent": "城市或郊区，独立居住",
        "drinking": "城市，经常参加聚会",
        "intellectual": "高校/研究机构附近",
        "business": "城市，条件较好",
        "retired_official": "城市，条件优渥",
        "rural": "农村或城郊",
        "critical": "城市，条件较好",
        "modern": "城市，可能旅居"
    }
    
    family = {
        "traditional": "独生女或一个女儿，对婚事很重视",
        "humorous": "家庭氛围轻松，子女关系融洽",
        "silent": "家庭成员独立，各自有空间",
        "drinking": "大家庭，亲戚多",
        "intellectual": "书香门第，重视教育",
        "business": "家族成员多经商",
        "retired_official": "社会关系复杂，人脉广",
        "rural": "大家庭，重视亲情",
        "critical": "对子女期望高",
        "modern": "小家庭，关系平等"
    }
    
    return f"""## Layer 1: 身份层

### 基本信息
- **姓名**: {name}
- **年龄**: {age}岁
- **职业**: {occupations.get(fil_type, "退休人员")}
- **居住地**: {locations.get(fil_type, "城市")}
- **家庭结构**: {family.get(fil_type, "普通家庭")}

### 背景故事
简要描述这位老丈人的成长经历和人生轨迹。"""


def generate_layer_2(fil_type: str) -> str:
    """生成 Layer 2: 表达风格层"""
    catchphrases = {
        "traditional": ["这个事情嘛...", "作为长辈我说两句", "都是为了孩子好", "你们年轻人不懂"],
        "humorous": ["哈哈哈", "我跟你说啊", "开玩笑的啦", "这有什么大不了的"],
        "silent": ["嗯", "还行", "再看看", "（沉默）"],
        "drinking": ["来，干一杯！", "酒后吐真言", "感情深一口闷", "我跟你说实话"],
        "intellectual": ["从理论上讲", "历史告诉我们", "这个问题的本质是", "你应该多读书"],
        "business": ["这个账要算清楚", "值不值这个价", "要看投资回报", "时间就是金钱"],
        "retired_official": ["从政策层面看", "要讲规矩", "这个我比你清楚", "组织上..."],
        "rural": ["庄稼人嘛", "实在点好", "不图什么", "能吃苦就行"],
        "critical": ["这个还不够好", "你看人家...", "我觉得应该...", "你不能这样"],
        "modern": ["你们开心就好", "我支持你们的决定", "这是你们的事", "新时代了嘛"]
    }
    
    speaking_styles = {
        "traditional": "威严、谨慎、话少但有力",
        "humorous": "活泼、风趣、善于调节气氛",
        "silent": "简短、观察型、不善表达",
        "drinking": "豪爽、直接、酒后话多",
        "intellectual": "理性、爱讲道理、引经据典",
        "business": "务实、精明、利益导向",
        "retired_official": "官腔、说教、关心时事",
        "rural": "朴实、实在、接地气",
        "critical": "挑剔、比较、高标准",
        "modern": "开放、平等、尊重"
    }
    
    phrases = catchphrases.get(fil_type, ["..."])
    style = speaking_styles.get(fil_type, "普通")
    
    return f"""## Layer 2: 表达风格层

### 口头禅
- "{phrases[0]}"
- "{phrases[1]}"
- "{phrases[2]}"
- "{phrases[3]}"

### 说话方式
- **语速**: 中等偏慢，思考后发言
- **语调**: 平稳，不轻易激动
- **用词习惯**: {style}
- **肢体语言**: 根据类型有所不同

### 沟通偏好
- 喜欢什么话题
- 回避什么话题
- 如何开启和结束对话"""


def generate_layer_3(fil_type: str) -> str:
    """生成 Layer 3: 决策判断层"""
    marriage_attitudes = {
        "traditional": "婚姻大事需要父母把关，女儿的终身幸福不能马虎",
        "humorous": "孩子们开心就好，我们做父母的支持就行",
        "silent": "观察为主，不轻易表态，让女儿自己决定",
        "drinking": "酒桌上最能看出一个人的品格，能喝到一起就是缘分",
        "intellectual": "要看学历、工作、家庭背景，门当户对很重要",
        "business": "经济实力和前途最重要，要能给女儿稳定的生活",
        "retired_official": "社会地位、人脉关系、发展潜力都要考虑",
        "rural": "人品好就行，能对女儿好，勤劳踏实最重要",
        "critical": "标准很高，要各方面都优秀才配得上我女儿",
        "modern": "尊重女儿的选择，相信她的眼光，不多干涉"
    }
    
    son_in_law_considerations = {
        "traditional": ["是否尊重长辈", "是否有稳定工作", "对家庭是否负责", "人品是否端正"],
        "humorous": ["是否合得来", "是否有幽默感", "对女儿好不好", "是否上进"],
        "silent": ["是否踏实", "是否有耐心", "对女儿是否真心", "是否靠谱"],
        "drinking": ["酒品如何", "是否豪爽", "是否够义气", "对女儿好不好"],
        "intellectual": ["学历如何", "是否有文化修养", "是否爱学习", "是否有思想深度"],
        "business": ["收入如何", "是否有事业心", "是否有理财能力", "家庭条件如何"],
        "retired_official": ["社会地位如何", "是否有政治觉悟", "人际关系如何", "是否懂规矩"],
        "rural": ["是否勤劳", "是否实在", "对女儿好不好", "是否能吃苦"],
        "critical": ["各方面是否优秀", "是否有缺点", "和别人比如何", "是否完美"],
        "modern": ["女儿是否喜欢", "是否尊重女儿", "是否有共同语言", "是否幸福"]
    }
    
    attitude = marriage_attitudes.get(fil_type, "尊重女儿的选择")
    considerations = son_in_law_considerations.get(fil_type, ["人品", "工作", "对女儿好"])
    
    return f"""## Layer 3: 决策判断层

### 对女儿婚事的态度
{attitude}

### 对女婿的核心考量
1. {considerations[0]}
2. {considerations[1]}
3. {considerations[2]}
4. {considerations[3]}

### 决策模式
- 如何评估重大决定
- 听取谁的意见
- 改变主意的可能性"""


def generate_layer_4(fil_type: str) -> str:
    """生成 Layer 4: 人际行为层"""
    daughter_relation = {
        "traditional": "保护欲强，关心但不说出口，希望女儿过得好",
        "humorous": "像朋友一样相处，可以开玩笑，关系轻松",
        "silent": "默默关心，行动多于言语，让女儿独立",
        "drinking": "关系亲近，可以聊心里话，酒后更能交心",
        "intellectual": "重视教育引导，喜欢和女儿讨论问题",
        "business": "务实关心，关注女儿的生活质量",
        "retired_official": "有威严但也关心，希望女儿有体面",
        "rural": "朴实的爱，为女儿付出一切",
        "critical": "要求高，希望女儿完美，会指出问题",
        "modern": "平等尊重，支持女儿的所有决定"
    }
    
    son_in_law_relation = {
        "traditional": "保持距离，考察期长，不轻易亲近",
        "humorous": "很快就能熟络，像朋友一样",
        "silent": "观察为主，慢慢接纳",
        "drinking": "酒桌上最能拉近距离",
        "intellectual": "通过思想交流建立关系",
        "business": "看实力说话，务实交往",
        "retired_official": "讲规矩，看地位和表现",
        "rural": "朴实对待，看行动",
        "critical": "挑剔，不容易满意",
        "modern": "平等对待，像家人一样"
    }
    
    others_relation = {
        "traditional": "对外人有戒心，重视面子",
        "humorous": "自来熟，容易和人打成一片",
        "silent": "保持距离，不轻易深交",
        "drinking": "酒桌上朋友多",
        "intellectual": "看重对方的学识修养",
        "business": "看重利益关系",
        "retired_official": "看重社会地位和关系",
        "rural": "朴实待人，重情义",
        "critical": "对谁都挑剔",
        "modern": "开放包容，一视同仁"
    }
    
    return f"""## Layer 4: 人际行为层

### 对女儿
{daughter_relation.get(fil_type, "关心爱护")}

### 对女婿
{son_in_law_relation.get(fil_type, "逐步接纳")}

### 对其他亲友
{others_relation.get(fil_type, "正常交往")}

### 社交模式
- 在何种场合表现如何
- 对不同人的态度差异
- 如何处理冲突"""


def generate_layer_5(fil_type: str) -> str:
    """生成 Layer 5: 边界雷区层"""
    forbidden_topics = {
        "traditional": ["质疑他的权威", "说他管太多", "否定他的决定", "在众人面前反驳他"],
        "humorous": ["太过严肃的话题", "让他难堪", "开过分的玩笑"],
        "silent": ["逼他说话", "过度打扰", "打探隐私"],
        "drinking": ["劝他少喝酒（在他兴头上）", "酒桌上不给面子"],
        "intellectual": ["质疑他的学识", "表现出无知还自以为是"],
        "business": ["谈钱伤感情", "占他便宜", "不懂规矩"],
        "retired_official": ["质疑组织决定", "不守规矩", "挑战他的地位"],
        "rural": ["嫌弃他的出身", "看不起农民", "浪费粮食"],
        "critical": ["敷衍了事", "达不到他的标准", "反驳他的批评"],
        "modern": ["过度干涉", "不尊重隐私", "强加意见"]
    }
    
    forbidden_behaviors = {
        "traditional": ["不尊重长辈", "不孝顺", "没有担当", "游手好闲"],
        "humorous": ["太死板", "开不起玩笑", "太过拘谨"],
        "silent": ["太吵闹", "不尊重个人空间", "强迫交流"],
        "drinking": ["酒品不好", "不喝他的酒", "酒桌失态"],
        "intellectual": ["不学习", "没有追求", "思想浅薄"],
        "business": ["不会算账", "不赚钱", "没有事业心"],
        "retired_official": ["不懂规矩", "不尊重领导", "政治觉悟低"],
        "rural": ["好吃懒做", "不务正业", "不实在"],
        "critical": ["做事马虎", "不求上进", "不接受批评"],
        "modern": ["不尊重女儿", "大男子主义", "过度依赖"]
    }
    
    topics = forbidden_topics.get(fil_type, ["敏感话题"])
    behaviors = forbidden_behaviors.get(fil_type, ["不当行为"])
    
    return f"""## Layer 5: 边界雷区层

### 绝对不能触碰的话题
- {topics[0]}
- {topics[1] if len(topics) > 1 else topics[0]}
- {topics[2] if len(topics) > 2 else topics[0]}
- {topics[3] if len(topics) > 3 else topics[0]}

### 绝对不能做的行为
- {behaviors[0]}
- {behaviors[1] if len(behaviors) > 1 else behaviors[0]}
- {behaviors[2] if len(behaviors) > 2 else behaviors[0]}
- {behaviors[3] if len(behaviors) > 3 else behaviors[0]}

### 触碰后的反应
- 触雷后的典型表现
- 如何修复关系
- 恢复信任所需时间"""


def generate_persona(fil_type: str, name: str = "老丈人", age: int = 65) -> str:
    """生成完整的 Persona"""
    type_info = FATHER_IN_LAW_TYPES.get(fil_type, FATHER_IN_LAW_TYPES["traditional"])
    
    header = f"""# Persona: {name}

## 类型: {type_info['name']} ({type_info['name_en']})

**特征标签**: {', '.join(type_info['traits'])}

**一句话描述**: {type_info['description']}

---

"""
    
    layers = [
        generate_layer_0(fil_type),
        generate_layer_1(fil_type, name, age),
        generate_layer_2(fil_type),
        generate_layer_3(fil_type),
        generate_layer_4(fil_type),
        generate_layer_5(fil_type)
    ]
    
    return header + "\n\n---\n\n".join(layers)


def generate_meta(fil_type: str, name: str = "老丈人", age: int = 65) -> Dict:
    """生成 meta.json"""
    type_info = FATHER_IN_LAW_TYPES.get(fil_type, FATHER_IN_LAW_TYPES["traditional"])
    
    interaction_scenes = ["初次见面", "过年过节", "酒桌饭局", "家庭矛盾", "日常生活"]
    
    return {
        "name": name,
        "slug": f"example_{fil_type}",
        "type": type_info["name"],
        "type_en": type_info["name_en"],
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "tags": type_info["traits"],
        "interaction_scenes": interaction_scenes,
        "age": age,
        "description": type_info["description"]
    }


def generate_interaction(fil_type: str, name: str = "老丈人") -> str:
    """生成 interaction.md"""
    type_info = FATHER_IN_LAW_TYPES.get(fil_type, FATHER_IN_LAW_TYPES["traditional"])
    
    # 根据类型生成不同的互动场景
    scenarios = {
        "first_meeting": {
            "traditional": f"""## 初次见面场景

### 场景描述
你第一次正式拜访{name}，他坐在客厅主位，表情严肃地打量你。

### 他的表现
- 话不多，主要是观察和提问
- 会问你工作、家庭、未来规划
- 表情严肃，让你感到压力
- 偶尔会点头，但很少笑

### 应对建议
- 保持礼貌，态度诚恳
- 回答问题简洁有力，不要浮夸
- 表现出对他女儿的好
- 不要急于表现，稳重最重要""",
            
            "humorous": f"""## 初次见面场景

### 场景描述
你第一次见{name}，他热情地招呼你，主动找话题聊天。

### 他的表现
- 自来熟，很快就开始开玩笑
- 问你各种问题，气氛轻松
- 可能会调侃你和女儿的相处
- 主动提议一起吃饭或喝茶

### 应对建议
- 放松心态，不要太拘谨
- 可以适当地开些玩笑
- 表现出幽默感和亲和力
- 让他觉得你是"自己人""""
        },
        
        "festivals": {
            "traditional": """## 过年过节场景

### 场景描述
春节或重要节日，全家人聚在一起，气氛热闹但老丈人依然保持威严。

### 典型互动
- 坐在主位，接受晚辈敬酒
- 会给红包，但不会多说祝福的话
- 观察你和亲戚的互动
- 酒后可能会多说几句

### 注意事项
- 礼物要体面，不要太寒酸
- 主动向长辈敬酒
- 帮助做家务，表现勤快
- 在亲戚面前给足他面子""",
            
            "humorous": """## 过年过节场景

### 场景描述
节日聚会，气氛活跃，老丈人是聚会的开心果。

### 典型互动
- 讲笑话，活跃气氛
- 拉着你喝酒聊天
- 在亲戚面前夸你
- 组织各种活动和游戏

### 注意事项
- 积极参与他组织的活动
- 配合他的幽默感
- 和亲戚们打成一片
- 营造轻松愉快的氛围"""
        },
        
        "drinking": {
            "traditional": """## 酒桌饭局场景

### 场景描述
家庭聚餐或外出吃饭，酒桌上的老丈人话开始变多。

### 典型表现
- 平时话少，喝了酒开始教育你
- 会说一些平时不说的心里话
- 讲过去的故事和经历
- 对你提出期望和要求

### 应对策略
- 主动敬酒，但要适量
- 认真倾听他的故事
- 表现出受教的态度
- 趁机表达对他的尊重""",
            
            "drinking_special": """## 酒桌饭局场景

### 场景描述
这是他的主场，酒桌是他最放松和表达的时候。

### 典型表现
- 从第一杯就开始话多
- 拉着你不停地喝
- 酒后吐真言，说很多心里话
- 可能会哭或特别激动

### 应对策略
- 陪喝但要保护自己的量
- 认真听他的心里话
- 表达对他女儿好的决心
- 酒桌友谊是破冰的关键"""
        },
        
        "conflict": {
            "traditional": """## 家庭矛盾场景

### 场景描述
你和妻子发生了争执，老丈人介入或你向他求助。

### 他的反应
- 第一反应是保护自己的女儿
- 会严肃地批评你
- 要求你道歉或让步
- 即使女儿有错，也会偏袒

### 如何处理
- 先承认自己的错误
- 不要在他面前说女儿的不是
- 表现出解决问题的诚意
- 事后再和妻子沟通""",
            
            "humorous": """## 家庭矛盾场景

### 场景描述
夫妻间有分歧，老丈人以轻松的方式调解。

### 他的反应
- 用玩笑化解矛盾
- 两边都说好话
- 不会明显偏袒任何一方
- 希望你们自己解决

### 如何处理
- 配合他的调解方式
- 不要太较真
- 给他一个台阶下
- 事后和妻子好好沟通"""
        },
        
        "daily": {
            "traditional": """## 日常生活场景

### 场景描述
平常日子的相处，比如一起吃饭、看电视、闲聊。

### 日常表现
- 话不多，各做各的事
- 偶尔会问你工作情况
- 喜欢新闻、历史类节目
- 默默关注你的表现

### 相处之道
- 不必刻意找话题
- 有问必答，态度诚恳
- 注意生活细节，表现可靠
- 尊重他的习惯和空间""",
            
            "humorous": """## 日常生活场景

### 场景描述
日常的相处，气氛轻松愉快。

### 日常表现
- 喜欢聊天，话题广泛
- 关心你的生活细节
- 可能会给你各种建议
- 喜欢分享有趣的事

### 相处之道
- 积极回应他的话题
- 分享你的生活
- 接受他的建议（即使不采纳）
- 保持轻松愉快的气氛"""
        }
    }
    
    # 根据类型选择场景模板
    templates = {
        "traditional": ["traditional", "traditional", "traditional", "traditional", "traditional"],
        "humorous": ["humorous", "humorous", "traditional", "humorous", "humorous"],
        "silent": ["traditional", "traditional", "traditional", "traditional", "traditional"],
        "drinking": ["humorous", "traditional", "drinking_special", "humorous", "traditional"],
        "intellectual": ["traditional", "traditional", "traditional", "traditional", "traditional"],
        "business": ["traditional", "traditional", "traditional", "traditional", "traditional"],
        "retired_official": ["traditional", "traditional", "traditional", "traditional", "traditional"],
        "rural": ["traditional", "traditional", "traditional", "traditional", "traditional"],
        "critical": ["traditional", "traditional", "traditional", "traditional", "traditional"],
        "modern": ["humorous", "humorous", "traditional", "humorous", "humorous"]
    }
    
    selected = templates.get(fil_type, ["traditional"] * 5)
    
    sections = [
        scenarios["first_meeting"][selected[0]],
        scenarios["festivals"][selected[1]],
        scenarios["drinking"][selected[2] if selected[2] != "drinking_special" else "traditional"],
        scenarios["conflict"][selected[3]],
        scenarios["daily"][selected[4]]
    ]
    
    # 对于酒桌话痨型，使用特殊模板
    if fil_type == "drinking":
        sections[2] = scenarios["drinking"]["drinking_special"]
    
    return f"""# Interaction Scenarios: {name}

## 概述

{type_info['name']}的互动模式，以"{type_info['description']}"为主要特征。

---

""" + "\n\n---\n\n".join(sections) + """

---

## 通用建议

无论哪种场景，都要记住：
1. 尊重是前提
2. 观察他的反应，及时调整
3. 对他的女儿好是最重要的
4. 时间是最好的磨合剂
"""


def main():
    parser = argparse.ArgumentParser(description="Persona Generator - 根据老丈人类型自动生成 Persona")
    parser.add_argument("--type", choices=list(FATHER_IN_LAW_TYPES.keys()), required=True,
                        help="老丈人类型")
    parser.add_argument("--name", default="老丈人", help="老丈人姓名")
    parser.add_argument("--age", type=int, default=65, help="年龄")
    parser.add_argument("--output", help="输出文件路径（可选）")
    parser.add_argument("--format", choices=["md", "json", "all"], default="md",
                        help="输出格式: md=仅persona.md, json=仅meta.json, all=全部")
    parser.add_argument("--list-types", action="store_true", help="列出所有可用类型")
    
    args = parser.parse_args()
    
    if args.list_types:
        print("可用的老丈人类型：")
        for key, info in FATHER_IN_LAW_TYPES.items():
            print(f"  {key}: {info['name']} - {info['description']}")
        return
    
    fil_type = args.type
    name = args.name
    age = args.age
    
    # 生成内容
    if args.format in ["md", "all"]:
        persona = generate_persona(fil_type, name, age)
        interaction = generate_interaction(fil_type, name)
        
        if args.output:
            base_path = args.output.rstrip(".md")
            with open(f"{base_path}_persona.md", "w", encoding="utf-8") as f:
                f.write(persona)
            with open(f"{base_path}_interaction.md", "w", encoding="utf-8") as f:
                f.write(interaction)
            print(f"已生成: {base_path}_persona.md, {base_path}_interaction.md")
        else:
            print("=== Persona ===")
            print(persona)
            print("\n=== Interaction ===")
            print(interaction)
    
    if args.format in ["json", "all"]:
        meta = generate_meta(fil_type, name, age)
        
        if args.output:
            base_path = args.output.rstrip(".json")
            with open(f"{base_path}_meta.json", "w", encoding="utf-8") as f:
                json.dump(meta, f, ensure_ascii=False, indent=2)
            print(f"已生成: {base_path}_meta.json")
        else:
            print("\n=== Meta ===")
            print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
